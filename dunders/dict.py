

class o:
    def __init__(self, **d): self.__dict__.update(d)

    def __setitem__(self, k, v): self.__dict__[k] = v

    def __getitem__(self, k): return self.__dict__[k]

    def __repr__(self): return 'o' + str(self.__dict__)


o = o(a = "a", b = "b", c = "c")
o.b = "h"
print(o.b);
print repr(o)
