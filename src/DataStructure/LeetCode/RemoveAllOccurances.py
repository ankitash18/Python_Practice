def remove_from_list(my_list, item):
    """
    Function that removes an item from a list
    """
    while (item in my_list):  # check if the element belongs to the list
        my_list.remove(item)  # remove THE FIRST occurrence of the element


list1 = [1, 2, 1, 1, 1, 1, 3]

## Calling the function and remove 1 from the list
remove_from_list(list1, 1)

print(list1)

countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']

## Removing duplicates from list by transforming it to a set and then back to a list
countries = list(set(countries))
countries.sort()  ## Sorting the list in place

print(countries)

with open('show_arp.txt', 'r', newline='') as f:
    ## Reading file in list (each line is list element)
    contents = f.read().splitlines()

    ## The argument newline='' is necessary only in Windows

    ## Eliminating the first item from the list (files header)
    contents = contents[1:]

    # Empty list that stores tuples like (ip, mac)
    ip_mac = list()

    # Iterating over the list(file contents) line by line
    for line in contents:
        ip = line.split()[1]  ## Getting the IP
        mac = line.split()[3]  ## Getting the MAC

        ## Adding the tuple to the ip_mac list
        ip_mac.append((ip, mac))

    print(
        ip_mac)  # [('192.168.122.10', 'aabb.cc00.0200'), ('192.168.122.20', 'aabb.cc00.0100'), ('192.168.122.30', 'aabb.cc00.0300')]

## show_arp.txt contents:
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  192.168.122.10          -   aabb.cc00.0200  ARPA   Ethernet0/0
# Internet  192.168.122.20          0   aabb.cc00.0100  ARPA   Ethernet0/0
# Internet  192.168.122.30          0   aabb.cc00.0300  ARPA   Ethernet0/0


## Assigning lambda expression to a variable called area
## length is lambda argument
area = lambda length: length ** 2

print(area(2.5))  # => 6.25




## The value of the constant PI with many decimal points
PI = 3.141592653589793

## Convert it to 4 decimal points, format() returns a string
PI = format(PI, '.5f')
PI = float(PI)  ## cast PI which is string to float

print(PI)  # => 3.14159










countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}

## List of keys sorted in alphabetical order
keys = sorted(countries.keys())

## Iterate over the keys and print the corresponding value of the dictionary
for k in keys:
    print(countries[k])

salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}

taxes = {k: v * 0.1 for k, v in salaries.items()}
print(taxes)