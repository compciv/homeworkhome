import data_helper
import json
from dateutil import parser as timeparser
import pytz

EASTCOAST_TIMEZONE = pytz.timezone('US/Eastern')

def get_tweets():
    """
    Knows how to get raw text from data_helper.read_data()
    Parses and deserializes it with the `json` library and
    returns a list of dict objects representing the full
    data as returned via Twitter/twarc

    Args:
        none
    Returns:
        <list>
    """
    txt = data_helper.read_data()
    tweets = json.loads(txt)
    return tweets

def get_simplified_tweets():
    """
    wrapper function around get_tweets() and extract_simple_tweet()

    Returns:
        <list>
    """
    simple_tweets = []
    for t in get_tweets():
        simple_tweets.append(simplify_tweet(t))
    return simple_tweets


def convert_timestamp_to_trump_datetime(timestamp):
    """
    Convert Twitter's unwieldly time format into a Python datetime
        object that is set to "Trump" time (i.e. Eastern timezone)

    Args:
        timestamp <str>: Twitter uses a semi-human-readable format for
              specifying time as a string:
               e.g. 'Wed Sep 20 10:14:30 +0000 2017'
    Returns:
        <datetime.datetime>: A Python datetime object with a timezone set
                 to the east coast, e.g.

    """
    dtime = timeparser.parse(timestamp)
    dtime = dtime.astimezone(EASTCOAST_TIMEZONE)
    return dtime


def simplify_tweet(tweet):
    """
    Given a dict that has all of the data for a tweet
    returned by Twitter API, returns a simplified/standardized
    version for easier use/browsing

    Args:
        tweet <dict>
    Returns:
        <dict> e.g.
    """
    simpletweet = {}
    simpletweet['id'] = tweet['id']
    simpletweet['favorite_count'] = tweet['favorite_count']
    simpletweet['full_text'] = tweet['full_text']
    simpletweet['retweet_count'] = tweet['retweet_count']
    simpletweet['created_at'] = convert_timestamp_to_trump_datetime(tweet['created_at'])

    return simpletweet


