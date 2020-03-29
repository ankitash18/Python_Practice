"""
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def longestsubstring(str):
    hashset =set()
    j =0
    i =0
    Max =0
    while j < len(str):
        if str[j]  not in  hashset:
            hashset.add(str[j])
            j +=1
            Max = max(len(hashset),Max)
        else:
            hashset.remove(str[i])
            i +=1

    return Max


s = 'abcabcbb'
a= longestsubstring(s)
print(a)
