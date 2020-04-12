import pickle

friends1 = {"Dan":[20,"London",323455],"maria":[25,"Madrid",4534566]}
friends2 = {"Andrie":[20,"Bucharest",323455],"Nina":[25,"Barcelona",4534566]}


friends = (friends1,friends2)

with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\friends.dat','wb') as f:
    pickle.dump(friends,f)


with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\friends.dat','rb') as f:
    obj=pickle.load(f)
    print(type(obj))
    print(obj)


#using json

import json

friends3 = {"Dan":[20,"London",323455],"maria":[25,"Madrid",4534566]}
#friends2 = {"Andrie":[20,"Bucharest",323455],"Nina":[25,"Barcelona",4534566]}

with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\friends.json','w') as f:
    json.dump(friends3,f,indent= 4)


json_stirng = json.dumps(friends3)
print(json_stirng)


#deserialize from json

with open('C:\\Users\\AShrivastava\\Desktop\\study\\sparkrockthejvm\\python\\friends.json','rt') as f:
    obj = json.load(f)
    print(obj)


# Serializing to file
def serialize(obj, file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    elif type == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj, f)
    else:
        print('Invalid serialization. Use pickle or json!')


# Deserializing from from to Python Object
def deserialize(file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            obj = pickle.load(f)
        return obj
    elif type == 'json':
        import json
        with open(file, 'r') as f:
            obj = json.load(f)
            return obj
    else:
        print('Invalid serialization. Use pickle or json!')


if __name__ == "__main__":
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}

    # Serializing using pickle
    serialize(d1, 'a.dat', 'pickle')

    # Deserializing
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')

    print('#' * 20)

    # serializing using pickle
    serialize(d1, 'a.json', 'json')

    # deserializing
    x = deserialize('a.json', 'json')
    # Notice how the tuple value was not preserved!
    print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}




