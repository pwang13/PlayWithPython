def items(x, depth=-1):
    if isinstance(x, (tuple, list)):
        # print(x)
        for y in x:
            for z in items(y, depth + 1):
                yield z
    else:
        yield x


# out = []
# for x in items([10, [20, 30],
#                 40,
#                 [(50, 60, 70),
#                  [80, 90, 100], 110]]):
#     out += [x]

out = [x for x in items ([10, [20, 30],
                40,
                [(50, 60, 70),
                 [80, 90, 100], 110]]) if x > 20]
print out
