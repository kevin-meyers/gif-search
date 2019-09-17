import json
import requests

API_KEY = 'NPCGNX1CXRCC'

SEARCH_LIMIT = 10


def search(query):
    r = requests.get(
        'https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s' % (
            query,
            API_KEY,
            SEARCH_LIMIT
        )
    )
    if r.status_code == 200:
        gifs_json = json.loads(r.content)
        return gifs_json

    return None

# TODO: Make trending request


def searchTrending():
    r = requests.get(
        'https://api.tenor.com/v1/trending?key=%s&limit=%s' % (
            API_KEY,
            SEARCH_LIMIT
        )
    )

    if r.status_code == 200:
        gif_json = json.loads(r.content)
        return gif_json
    return None
