from contextlib import contextmanager

@contextmanager
def tag(name, content):
    print "<%s>" % name
    yield content
    print "</%s>" % name

with tag("h1", "foo") as content:
    print content