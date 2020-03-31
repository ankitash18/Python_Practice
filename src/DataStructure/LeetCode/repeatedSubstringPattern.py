"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
"""


def repeatedSubstringPattern(s):
    length = len(s)
    for i in range(length//2,0,-1):
        if length%i== 0:
            repeatedtimes = length//i
            sub = s[:i]
            s1 = sub*repeatedtimes
            print(s1)

            if (s1 == s):
                return True

    return False


s = "abcabc"
a = repeatedSubstringPattern(s)
print(a)





def repeatedSubstringPattern(s) :
    h, token = len(s) // 2, ''
    print(h)


    for i in range(h):
        token += s[i]
        print(token)
        multiplier = len(s) // len(token)
        print(multiplier)
        print(token * multiplier)
        if token * multiplier == s: return True

    return False


s1 = "abcabc"
b= repeatedSubstringPattern(s1)
print(b)