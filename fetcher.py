import requests

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

# def scrapetweets(city,option):
    
#     new_search = "verified "+ city +" "+ option  +" -'not verified' -'un verified' -filter:retweets -urgent -unverified -needed -required -need -needs -requirement "
#     link=[]

#     for tweet in tweepy.Cursor(api.search, q=new_search, lang="en",count=100,since=dt).items(5):

#         try: 
#             data = [tweet.id]
#             status = api.get_status(tweet.id)
#             created_at = status.created_at
#             temp_time = created_at.strftime(format)
#             final_time = time_converter(str(temp_time))
#             link.append(f"https://twitter.com/anyuser/status/"+str(data[0]) + " " + str(final_time))
        
#         except tweepy.TweepError as e:
#             print(e.reason)
#             continue

#         except StopIteration:
#             break

#     return link
