import random

r = random.random
rseed = random.seed


class Some:
    def __init__(self, max=8):
        self.n, self.any, self.max = 0, [], max

    def __iadd__(self, x):
        self.n += 1
        now = len(self.any)
        if now < self.max:
            self.any += [x]
        elif r() <= now / self.n:
            self.any[int(r() * now)] = x
        return self

some = Some()
some += 3
print(some.any)

