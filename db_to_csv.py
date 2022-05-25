"""
Script to output customer details from the database column
Data is exported to a csv file for the ease of using it on the clustering model
"""

import pandas as pd
from pymongo import MongoClient
from keys import detailsDict

csv_file = 'data.csv'

client = MongoClient(detailsDict.db.URL)
db = client[detailsDict.db.DATABASE]
col = db[detailsDict.db.COLLECTION]

all_tweets = list(col.find())
print(len(all_tweets))
print(all_tweets[0])

df = pd.DataFrame(all_tweets)
df.drop(columns="_id")
df.to_csv(csv_file, index=False)
