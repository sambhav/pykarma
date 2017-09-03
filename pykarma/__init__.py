# -*- coding: utf-8 -*-
import requests
import praw

from functools import lru_cache

from bs4 import BeautifulSoup
from ratelimit import rate_limited


API_URL = "http://karmadecay.com/search"
reddit = praw.Reddit(client_id="_MyO9rFo5vRsqg", client_secret=None, user_agent="samj1912/KD API")

class KDResuts():

    def __init__(self, soup, fetch_praw=False):
        self.soup = soup
        self.fetch_praw = fetch_praw
        self.original = self.find_submission(self.soup.find(class_="s"))

        # Finds all results before the "Less Similar" boundry tag
        self._break_tag = self.soup.find(class_="ls")
    
    def find_submission(self, obj):
        try:
            result = obj.select_one(".title > a").get('href')
            if self.fetch_praw:
                result = reddit.submission(url=result)
            return result
        except (TypeError, KeyError, AttributeError):
            return None

    def __iter__(self):
        for sibling in self._break_tag.find_all_previous(class_="result"):
            yield self.find_submission(sibling)      


@rate_limited(1)
@lru_cache(maxsize=100)
def find(url, fetch_praw=False):
    """
    Searches a URL on Karma Decay and returns a PRAW Submission object.

    Args:
        url (str): URL for the object to reverse-search.
        fetch_praw (:obj:`bool`, optional): Indicates return type. If True return PRAW Submission objects.
            Else returns URLs of the results. Defaults to False.

    Return:
        iter: An iterator for matched results.

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
    return KDResuts(soup, fetch_praw=fetch_praw)
