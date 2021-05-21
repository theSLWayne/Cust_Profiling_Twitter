# Customer Profiling for E-Marketing Platforms Using Twitter

## Introduction

A project to help comapnies to cluster their customers based on their opinions and purchasing habits using Tweets of their customers posting about a certain company.

This approach to get information about customers to cluster them do not require usage of loyalty cards or mobile applications(aside from Twitter, of course) as used in many customer profiling cases.

The program created in this repository is an attempt to profile customers of a certain company with the aid of deep learning(Natural Language Processing), clustering and Twitter API.

**All data retrieved from Twitter API will not violate privacy of any user. The program takes ONLY the information that can be used in profiling them. The information taken about the user will not in any way suffice to figure out the identity of a single user at any case.**

## Workflow

1. The system will retrieve Tweets mentioning the company Twitter handle or including a specific set of keywords.

2. Retrieved Tweets will be analyzed to determine the sentiment and subjectivity of the Tweet.

3. Determined sentiment analysis results, long with other few details about the author of the Tweet(again, no privacy violation) will be stored in a database to be used by the clustering program.

4. Clustering program will take information from the database and profile similar customers together and store clustering details in the database.

5. Details about clusters of customers can be accessed by the marketing team and can do direct, effective advertising to customers using Twitter API.
