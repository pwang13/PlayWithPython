def remove_whitespaces(a_string):
    import string
    str = [x for x in a_string if x not in string.whitespace]
    return "".join(str)


def lines(string):
    tmp = ''
    for ch in string:
        if ch == "\n":
            yield tmp
            tmp = ''
        else:
            tmp += ch
    if tmp:
        yield tmp

def atleast_20(string):
    return [remove_whitespaces(line) for line in lines(string) if remove_whitespaces(line) and len(line) > 20]

print atleast_20("h hh \n"
                         "\n"
                         "   \n"
                         "f jd jdjdk k djdfkaljfdkjfsljf"
                         "")
