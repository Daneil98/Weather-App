import requests


headers = {
        'Content-Type': 'application/json',
    }

def get_meta_data(location):
    requestResponse = requests.get("http://api.weatherapi.com/v1/current.json?key=46723aaad5a94c3c961130530232408&q={}&aqi=no".format(location), headers= headers)
    return requestResponse.json()
    

