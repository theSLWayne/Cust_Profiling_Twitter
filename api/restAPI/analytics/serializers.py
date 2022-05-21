from rest_framework import serializers
from analytics.models import Customer, Cluster

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id',
                'user_id',
                'polarity',
                'subjectivity',
                'verified',
                'protected',
                'favorites',
                'retweets',
                'no_tweets',
                'no_tweets_total',
                'followers',
                'cluster'
                )

class ClusterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cluster
        fields = ('cluster',
                'customers',
                'avg_polarity',
                'avg_subjectivity',
                'no_verified',
                'no_protected',
                'avg_favorites',
                'avg_tweets',
                'avg_account_tweets',
                'avg_followers'
                )