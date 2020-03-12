#Import Counter class from collections module.
#split the inout string ,it will return the list of words

from collections import Counter


data_set = """Welcome to the world of Geeks  This portal has been created to provide well written well 
thought and well explained solutions for selected questions 
If you like Geeks for Geeks and would like to contribute 
here is your chance You can write article and mail your article 
to contribute at geeksforgeeks org See your article appearing on 
the Geeks for Geeks main page and help thousands of other Geeks. """


# split() returns list of all the words in the string

data_split = data_set.split()

# Pass the split_it list to instance of Counter class.
counter = Counter(data_split)


print(data_split)

print(counter)

#most common words

most_occur = counter.most_common(10)

print(most_occur)