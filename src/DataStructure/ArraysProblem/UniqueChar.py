def uni_char(s):
    return len(set(s)) == len(s)  #using set datastructure


a = uni_char("abcade")

print(a)

def uni_char2(s):
    char = set()

    for let in s:
        if let in char:
            return False
        else:
            char.add(let)

    return True


b = uni_char("abcde")

print(b)
