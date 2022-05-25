"""
Retrieve old tweets containing the search queries
"""

import tweepy
from textblob import TextBlob
from keys import detailsDict
from pymongo import MongoClient
import tensorflow as tf
import pickle

details = detailsDict

TWITTER_APP_KEY = details.keysDict.TWITTER_APP_KEY
TWITTER_APP_SECRET = details.keysDict.TWITTER_APP_SECRET
TWITTER_KEY = details.keysDict.TWITTER_KEY
TWITTER_SECRET = details.keysDict.TWITTER_SECRET

# Set authentication for Twitter API
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)

api = tweepy.API(auth)

# Setup database connection
dbclient = MongoClient(details.db.URL)
db = dbclient[details.db.DATABASE]
col = db[details.db.COLLECTION]

# Set keywords
search_words = details.queries.KEYWORD
# Filter out retweets
search_query = search_words + " -filter:retweets"

# Retrieve tweets from the API
for tweet in tweepy.Cursor(
    api.search_tweets,
    q=search_query,
    count=details.queries.COUNT,
    lang="en",
    since_id=0,
).items():
    # Using TextBlob to get subjectivity score of the tweet
    tweet_text = TextBlob(tweet.text)
    # Loading trained sentiment analysis model to get polarity of the tweet
    sentiment_model = tf.keras.models.load_model("./Models/sentiment140_bert")
    polarity = tf.sigmoid(sentiment_model.predict(tweet.text))

    # Check whether the user that posted the tweet is already in the database
    # If yes, update their existing record in the database
    if col.find({"user_id": tweet.user.id}).count() >= 1:
        # Get database record of the user
        user_profile = col.find_one({"user_id": tweet.user.id})

        # Increment tweet count
        new_tweet_count = user_profile["no_tweets"] + 1

        # Create new user profile
        tweet_profile = {
            "user_id": tweet.user.id,

            # Calculate new average polarity
            "polarity": (
                user_profile["polarity"] * user_profile["no_tweets"] + polarity
            )
            / new_tweet_count,

            # Calculate new average subjectivity
            "subjectivity": (
                user_profile["subjectivity"] * user_profile["no_tweets"]
                + tweet_text.sentiment.subjectivity
            )
            / new_tweet_count,
            "verified": 1 if tweet.user.verified else 0,
            "protected": 1 if tweet.user.protected else 0,

            # Update total favorites count
            "favorites": user_profile["favorites"] + tweet.favorite_count,

            # Update total retweets count
            "retweets": user_profile["retweets"] + tweet.retweet_count,
            "no_tweets": new_tweet_count,
            "no_tweets_total": tweet.user.statuses_count,
            "followers": tweet.user.followers_count,
        }

        # Preprocessing for clustering model
        preprocessor = pickle.load(open("./Models/pipeline.pkl", "rb"))
        preprocessed = preprocessor.transform(tweet_profile)

        # Predicting the cluster of the updated profile
        cluster_model = pickle.load(open("./Models/cluster_model.pkl", "rb"))
        cluster = cluster_model.predict(preprocessed)

        # Add the cluster to user profile
        tweet_profile["cluster"] = cluster

        # Update user record on the database
        x = col.update_one({"user_id": tweet.user.id}, {"$set": tweet_profile})

        print(x.upserted_id)

    # If the user is not already in the database
    else:
        # Create a new user profile
        tweet_profile = {
            "user_id": tweet.user.id,
            "polarity": polarity,
            "subjectivity": tweet_text.sentiment.subjectivity,
            "verified": 1 if tweet.user.verified else 0,
            "protected": 1 if tweet.user.protected else 0,
            "favorites": tweet.favorite_count,
            "retweets": tweet.retweet_count,
            "no_tweets": 1,
            "no_tweets_total": tweet.user.statuses_count,
            "followers": tweet.user.followers_count,
        }

        # Preprocess for clustering model
        preprocessor = pickle.load(open("./Models/pipeline.pkl", "rb"))
        preprocessed = preprocessor.transform(tweet_profile)

        # Predicting the cluster of the user profile
        cluster_model = pickle.load(open("./Models/cluster_model.pkl", "rb"))
        cluster = cluster_model.predict(preprocessed)

        # Add cluster to the user profile
        tweet_profile["cluster"] = cluster

        # Inser t user profile into the database
        x = col.insert_one(tweet_profile)
        print(x.inserted_id)
