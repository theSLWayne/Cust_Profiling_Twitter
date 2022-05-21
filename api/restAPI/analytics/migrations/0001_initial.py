# Generated by Django 3.2.9 on 2021-12-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=300)),
                ('polarity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('subjectivity', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('verified', models.IntegerField(default=0)),
                ('protected', models.IntegerField(default=0)),
                ('favorites', models.IntegerField(default=0)),
                ('retweets', models.IntegerField(default=0)),
                ('no_tweets', models.IntegerField(default=0)),
                ('no_tweets_total', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
            ],
        ),
    ]
