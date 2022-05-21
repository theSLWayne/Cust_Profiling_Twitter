from django.db import models

# Create your models here.

class Customer(models.Model):
    user_id = models.CharField(max_length=300, blank=False, default='')
    polarity = models.DecimalField(blank=False, default=0.0, decimal_places=3, max_digits=10)
    subjectivity = models.DecimalField(blank=False, default=0.0, decimal_places=3, max_digits=10)
    verified = models.IntegerField(blank=False, default=0)
    protected = models.IntegerField(blank=False, default=0)
    favorites = models.IntegerField(blank=False, default=0)
    retweets = models.IntegerField(blank=False, default=0)
    no_tweets = models.IntegerField(blank=False, default=0)
    no_tweets_total = models.IntegerField(blank=False, default=0)
    followers = models.IntegerField(blank=False, default=0)
    cluster = models.IntegerField(blank=False, default=0)

class Cluster(models.Model):
    cluster = models.IntegerField(blank=False, default=0)
    customers = models.IntegerField(blank=False, default=0)
    avg_polarity = models.DecimalField(blank=False, default=0.0, decimal_places=4, max_digits=10)
    avg_subjectivity = models.DecimalField(blank=False, default=0.0, decimal_places=4, max_digits=10)
    no_verified = models.IntegerField(blank=False, default=0)
    no_protected = models.IntegerField(blank=False, default=0)
    avg_favorites = models.DecimalField(blank=False, default=0.0, decimal_places=4, max_digits=15)
    avg_tweets = models.DecimalField(blank=False, default=0.0, decimal_places=4, max_digits=15)
    avg_account_tweets = models.DecimalField(blank=False, default=0.0, decimal_places=4, max_digits=15)
    avg_followers = models.IntegerField(blank=False, default=0)
