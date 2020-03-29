s = "a  "

s1 = s.split(' ')
print(s1)

print(len(s1[-1]))


def lastlenth(str):
    count =0
    state = False

    for i in reversed(range(0,len(str))):
        print(i)
        if not state:
            if s[i] is not ' ':
               # print("came hre")
                state = True

        if state:
           # print("here",s[i])
            if s[i] == ' ':
                print("came here")
                return count
       # print(" here")
        count +=1

    return count


a= "a "
a1 = lastlenth(a)

print(a1)


def lengthOfLastWord( s):
    if len(s) == 0: return 0
    splitted_str = s.split(' ')
    for idx in reversed(range(len(splitted_str))):
        s_len = len(splitted_str[idx])
        if s_len > 0:
            return s_len
    return 0


a1 = lengthOfLastWord("     ")
print(a1)


def lengthOfLastWord1(s):
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            while s[i] != ' ' and i >= 0:
                count += 1
                i -= 1
            break
    return count


a12 = lengthOfLastWord("      ")
print(a12)
