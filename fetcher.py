import requests
import os
from dotenv import load_dotenv
import tweepy
import time





def all():
    data=requests.get("https://disease.sh/v3/covid-19/all").json()
    world_data={
        "cases":data["cases"],"todayCases":data["todayCases"],
        "deaths":data["deaths"],"todayDeaths":data["todayDeaths"],
        "recovered":data["recovered"],"todayRecovered":data["todayRecovered"],
        "active":data["active"],
        "critical":data["critical"],
        "affectedCountries":data["affectedCountries"]    
    }
    return world_data

def specific_data(location):
    data=requests.get(f"https://disease.sh/v3/covid-19/countries/{location}").json()
    try:
        country_data={
            "country":data["country"],"flag":data["countryInfo"]["flag"],   
            "cases":data["cases"],"todayCases":data["todayCases"],
            "deaths":data["deaths"],"todayDeaths":data["todayDeaths"],
            "recovered":data["recovered"],"todayRecovered":data["todayRecovered"],
            "active":data["active"], 
        }
        return (True,country_data)
    except:
         return (False,"error")

def get_tweets(city, resource):

    load_dotenv()
    consumer_secret = os.getenv('consumer_key')
    consumer_key = os.getenv('consumer_secret')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets_list=[]
    query = "verified {} {} -not verified -un verified -urgent -unverified -needed -required -need -needs".format(city, resource)
    count = 15

    try:
        tweets = api.search(q = query,count = count, tweet_mode = 'extended')
        print(tweets)
        #tweets_list = [[tweet.created_at, tweet.id, tweet.full_text] for tweet in tweets]
        #tweets_df = pd.DataFrame(tweets_list)
        
        print(tweets)
        for tweet in tweets:
            if 'retweeted_status' in tweet._json:
                tweets_list.append([tweet.id_str, tweet.user.name, tweet.user.screen_name, tweet._json['retweeted_status']['full_text']])
            else:
                tweets_list.append([tweet.id_str, tweet.user.name, tweet.user.screen_name, tweet.full_text])
    except BaseException as e:
        print("failed", str(e))
        time.sleep(3)

    return tweets_list

