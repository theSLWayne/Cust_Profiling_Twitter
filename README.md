# Customer Profile Analysis using Twitter Analytics

## 1. Introduction

This project is designed to create an API that can be used by companies and brands to gather information about what people are posting about them on one of the most popular social media platforms, Twitter.

This approach to get information about customers to cluster them do not require usage of loyalty cards, surveys, or mobile applications(aside from Twitter, of course) as used in many customer profiling cases.

The program created in this repository is an attempt to profile customers of a certain company with the aid of deep learning(Natural Language Processing), clustering and Twitter API.

**All data retrieved from Twitter API will not violate privacy of any user. The program takes ONLY the information that can be used in profiling them. The information taken about the user will not in any way suffice to figure out the identity of a single user at any case.**  

## 2. Process Workflow

1. The system will retrieve Tweets mentioning the company Twitter handle or including a specific set of keywords.

2. Retrieved Tweets will be analyzed to determine the sentiment and subjectivity of the Tweet.

3. Determined sentiment analysis results, long with other few details about the author of the Tweet(again, no privacy violation) will be stored in a database to be used by the clustering program.

4. Clustering program will take information from the database and profile similar customers together and store clustering details in the database.

5. Details about clusters of customers can be accessed by the marketing team and can do direct, effective advertising to customers using Twitter API.


## 3. Components

This project is made up from a couple of components that provide services along the process workflow. Below is a high-level overview of the project's components and their interactions.

<div style='text-align: center'>
![Components of the project not available at the moment.](docs/components.png)
</div>
### 3.1. Twitter API

Twitter API was used to retrieve Tweets from users. 

### 3.2. Processing Tweets

### 3.3. Database

### 3.4. Django REST API

## Files



