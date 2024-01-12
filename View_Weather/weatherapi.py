import requests


headers = {
        'Content-Type': 'application/json',
    }

def get_meta_data(location):
    requestResponse = requests.get("http://api.weatherapi.com/v1/current.json?'your key'={}&aqi=no".format(location), headers= headers)
    return requestResponse.json()
    

