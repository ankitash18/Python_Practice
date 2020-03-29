"""
Given an array of strings, group anagrams together.
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


a= 'eat'


#word = ''.join(sorted(a))
#print(word)

def anagrams(strs):
    d = {} #map to sotry key as a sorte string and all its anagram string

    ans = [] #list[list[stirng]]

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word  in d:
            d[sorted_word].append(word)
        else:
            d[sorted_word] = [word]

    for key in d:
        ans.append(d[key])

    return ans



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = anagrams(strs)
print(res)

def groupAnagrams(strs):
    # Group List of arrays of words
    groupList = []

    # Dictionary with the sorted word as the key and the array of actual words as the value
    sortedWordDict = {}

    # For loop that adds the sorted words as keys and array of words as values to the sortedWordDict
    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord in sortedWordDict:
            sortedWordDict[sortedWord].append(word)
        else:
            sortedWordDict[sortedWord] = [word]

    # For loop that adds the arrays of words to the groupList of arrays
    for x in sortedWordDict.values():
        groupList.append(x)

    return groupList


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
print(res)