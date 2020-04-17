#counter
from collections import Counter

deice_tem = [1,2,1,4,1,3,5,4,4,4,4]

mostuseddevice = Counter(deice_tem)
print(mostuseddevice)

#defaultdict


#default dict never raies key erorr

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_mater  ={}

for coworked,place in coworkers:
    if coworked not in alma_mater:
        alma_mater[coworked]=[]
    alma_mater[coworked].append(place)


#or using default dict

alma_maters = defaultdict(list)

for coworked,place in coworkers:
        alma_maters[coworked].append(place)


print(alma_maters['Rolf'])
print(alma_maters['Anne'])


#named tuple

from collections import namedtuple

account = ('checking',1250)
Account =namedtuple('Account',['name','balance'])

print(Account.name)

#deque

from collections import deque
#thread safe
friends = deque(('Rolf','charlie','Ana'))
friends.append('jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()

print(friends)



