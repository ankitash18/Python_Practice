#don not ue slice or use iteraion/use recursion

# 'abc' -> 'c' + rev('ab') -> 'c' + 'b' + rev('a') -> 'c' +'b'+'a'
def reversestr(s):
    #base case
    if len(s) == 1:
        return s
    else:
        return reversestr(s[1:]) + s[0]


a= reversestr('hello world')
print(a)