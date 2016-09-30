def remove_whitespaces(a_string):

    import string
    str = [x for x in a_string if x not in string.whitespace]
    return ".".join(str)

print remove_whitespaces("haha ha hhh hahah")