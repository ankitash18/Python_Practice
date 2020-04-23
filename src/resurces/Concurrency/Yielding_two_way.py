from collections import deque

friends =deque(('Rolf','Jose','Charlie','jen','Anna'))

def get_frnd():
    yield  from friends


c = get_frnd()

print(next(c))
print(next(c))

def greet(g):
    while True:
        try:
            friend= next(g)
            yield f'hello {friend}'
        except StopIteration:
            pass


frien_gen = get_frnd()
g= greet(frien_gen)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

