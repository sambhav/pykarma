# pykarma
Unofficial Python API wrapper for [karmadecay.com](http://karmadecay.com)

## Usage
```python
from pykarma import find

result = find("http://i.imgur.com/OOFRJvr.gifv")
print(result.score)
```
The API returns a [PRAW Submission Object](http://praw.readthedocs.io/en/latest/code_overview/models/submission.html).
Read the [PRAW documentation](http://praw.readthedocs.io/en/latest/code_overview/praw_models.html) to learn how to use it. 

## Installation

* From pip:

        pip install pykarma

* From source:
        
        git clone https://github.com/samj1912/pykarma
        python setup.py install