import requests

def make_request():
    response = requests.get('https://google.com')
    return response.status_code