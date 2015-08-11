import sys
import requests
from urlparse import urlparse

## Read lines from stdin
for line in sys.stdin:
    payload = {'q': line}
    r = requests.get("http://search.labs.crossref.org/dois", params=payload)
    r2 = requests.get("http://api.crossref.org/works" + urlparse(r.json()[0]['doi'])[2] + "/transform/application/x-bibtex")
    print(r2.text)
