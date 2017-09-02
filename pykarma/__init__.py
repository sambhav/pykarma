# -*- coding: utf-8 -*-
import requests
import praw

from functools import lru_cache

from bs4 import BeautifulSoup
from ratelimit import rate_limited


API_URL = "http://karmadecay.com/search"
reddit = praw.Reddit(client_id="_MyO9rFo5vRsqg", client_secret=None, user_agent="samj1912/KD API")


@rate_limited(1)
@lru_cache(maxsize=100)
def find(url, less_similar=False):
    """
    Searches a URL on Karma Decay and returns a PRAW Submission object.

    Args:
        url (str): URL for the object to reverse-search.
        less_similar (:obj:`bool`, optional): Include less similar results. Defaults to False.

    Return:
        PRAW Submission object: Matched reddit submission if match found else None.

    """

    payload = {
        'kdtoolver': 'b1',
        'q': url
    }
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) KD API Search'
    }

    request = requests.get(API_URL, params=payload, headers=headers)
    soup = BeautifulSoup(request.content, "html.parser")
    match = soup.select_one("tr.s > td.info > div.title > a")

    if less_similar and not match:
        match = soup.select_one(".result > td.info > div.title > a")

    if not match:
        return None

    result = reddit.submission(url=match.get('href'))

    return result
