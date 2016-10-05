from contextlib import contextmanager
from contextlib import closing
import urllib

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

with closing(urllib.urlopen('http://www.python.org')) as page:
    for line in page:
        print line