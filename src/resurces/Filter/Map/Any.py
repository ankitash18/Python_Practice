#filter method


def starts_with_r(friend):
    return friend.startswith('R')



friend = ['Rolf','Jose','Randy','Anna','Mary']

r = filter(starts_with_r,friend)

#or us lamba

r1 = filter(lambda x:x.startswith('R'),friend)
print(next(r))
print(next(r))


def my_custom_filter(func,iterbale):
    for i in iterbale:
        if func(i):
            yield  i


r2 = my_custom_filter(lambda x:x.startswith('R'),friend)

friends_lower=map(lambda x:x.lower(),friend)

friends_lower1 = (friend.lower() for friend in friend)

print(friends_lower)
print(next(friends_lower))
print(friends_lower1)

print(next(friends_lower1))


