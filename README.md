# pykarma
Unofficial Python API wrapper for [karmadecay.com](http://karmadecay.com)

## Usage
```python
from pykarma import find

# Fetch only the submission URLs of the matches
results = find("http://i.imgur.com/OOFRJvr.gifv")
for result in results:
    print(result)

# Fetch matches within a specific subreddit
results = find("http://i.imgur.com/OOFRJvr.gifv", subreddit="example")
for result in results:
    print(result)

# Fetch matches within multiple subreddits
results = find("http://i.imgur.com/OOFRJvr.gifv", subreddit=["example", "bottesting"])
for result in resultS:
    print(result)

# Fetch complete details about the matches
results = find("http://i.imgur.com/OOFRJvr.gifv", fetch_praw=True)
for result in results:
    print(result.url)
    print(result.score)

```
You can also combine `fetch_praw` and `subreddit` to get submission objects on a specific subreddit

The API returns a [PRAW Submission Object](http://praw.readthedocs.io/en/latest/code_overview/models/submission.html).
Read the [PRAW documentation](http://praw.readthedocs.io/en/latest/code_overview/praw_models.html) to learn how to use it. 

## Installation

* From pip:

        pip install pykarma

* From source:
        
        git clone https://github.com/samj1912/pykarma
        python setup.py install
