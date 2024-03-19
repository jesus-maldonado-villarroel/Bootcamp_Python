import requests
import json


def request_json(url):
    return json.loads(requests.get(url).text)
