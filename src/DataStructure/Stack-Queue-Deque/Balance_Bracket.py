def balance_bracket(s):
    if len(s)%2 != 0:
        return False

    opening = set('({[')
    matches = set([( '(' ,')'),('[',']'),('{','}')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) ==0:
                return False

            last_open = stack.pop()

            if (last_open,paren) not in matches:
                return False

    return len(stack) == 0


a = balance_bracket('{{}}')

print(a)

#using for loop



def isvalid(s):
    if len(s) % 2 != 0:
        return False

        stk =[]


    for i in range(0,len(s)):
        print((len(stk)-1))
        if s[i] =='(' or s[i] == '{' or s[i] == '[':
            stk.append(s[i])
        elif (len(stk) != 0 and s[i] ==')' and stk[len(stk)-1] == '(' ):
                stk.pop()
        elif (len(stk) != 0 and s[i] =='}' and stk[len(stk)-1] == '{' ):
            stk.pop()
        elif (len(stk) != 0 and s[i] ==']' and stk[len(stk)-1] == '[' ):
            stk.pop()
        else:
            stk.append(s[i])

    return len(stk) == 0

b = isvalid('{{}}')

print(b)
