import csv
import twitter
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from maplecroft.models import Countries


class Index(TemplateView):
    template_name = "maplecroft/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # returns list of tweets
        tweet_list = get_tweets()
        countries = Countries.objects.all()
        country_tweet_dict = {}
        for country in countries:
            for tweet in tweet_list:
                # removes hashtags to recognise country
                tweet_no_hashtag = tweet.replace('#', ' ')
                # cleans up the tweets html, in order to be placed onto google maps
                new_tweet = tweet.replace('\n', ' ')
                # splits the tweet list in order to compare to countries
                new_tweet_list = tweet_no_hashtag.split(' ')
                if country.country in new_tweet_list:
                    # dictionary with country name and associated tweets
                    country_tweet_dict[country] = mark_safe(new_tweet)
        context['countries'] = country_tweet_dict
        return context

# imports the csv file into Country model


def import_data():
    with open('countries.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != '':
                _, created = Countries.objects.get_or_create(
                   country=row[0],
                   country_abbreviation=row[1],
                   longitude=row[2],
                   latitude=row[3],
                   )

# Gets tweets from @MaplecroftRisk


def get_tweets():
    api = twitter.Api(consumer_key='x5oUWZ5WiKtxlvBmyFtBq1COP',
                      consumer_secret='3IR2h7UpTUjwKxDN7wkpkE4jjyOWZpk9R4Pcl5nIl0XgDJi3zb',
                      access_token_key='959215696998748160-fa9KMlBT5v4AurltL8UoqFeKDoMO7A3',
                      access_token_secret='qMRPFAyRrT5g7ijPwvJWq0vxu8fW9n1c3Cfmm5OWbVNyU')
    tweet = api.GetUserTimeline(screen_name='@MaplecroftRisk')[:10]
    tweet_list = [s.text for s in tweet]
    return tweet_list
