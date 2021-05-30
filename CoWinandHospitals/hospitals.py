def return_hospitals(query):
    api_key="your api key"
    return_text="These are the 5 hospitals near you\n"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url + 'query=' + query +'&key=' + api_key)
    x = r.json()
    y = x['results']
    for i in range(5):
        return_text+="{}.{}\n".format(i+1,y[i]['name'])
    return return_text