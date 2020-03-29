#We ramdomly pick a string from 'strs' as 'bench_mark' [0]
#Lets say the 'bench_mark' is 'flower'
#We compair 'f', 'fl', 'flo'... to every other string [1]
#If any string does not match, we return the longest common prefix [2]
#In ths case the whole 'bench_mark' is actually the longest common prefix [3]
#We need to return the 'bench_mark'


def commonprefix(str):
    if len(str) == 0:
        return ""

    bench_mark = str[0] #0
    print(f"bench_mark si {bench_mark}")

    for i in range(1,len(bench_mark)+1): #1
        common_string = bench_mark[:i]
        print(f"common_string si {common_string}")
        for s in str:
            print(f"s[:i] {s[:i]}")
            if s[:i] != common_string:#2
                print(f"hrehre when s[:i] is {s[:i]}")
                return bench_mark[:i-1]

    return bench_mark #3



input = ["flower","flo","flon"]

a = commonprefix(input)

print(a)