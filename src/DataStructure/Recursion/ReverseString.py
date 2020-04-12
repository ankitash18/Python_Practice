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

## List of Words
words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']

## List comprehension that constructs a list of palindromes from names list
palindromes = [items for items in words if items.lower() == items[::-1].lower()]

print(palindromes)