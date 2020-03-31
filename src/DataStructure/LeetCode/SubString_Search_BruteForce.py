def substring_search(str,pattern):
    index = -1
    for i in range(0,(len(str)-len(pattern))+1):
        if index == -1:
            j =0

            while(j <len(pattern) and str[i+j]== pattern[j]):
                print(f"{j}...{i}...{str[i+j]}....{pattern[j]}")
                j +=1


            if (j == len(pattern)):
                index = i

    return index


str ="Hi,there hello"
pattern = "there"

a = substring_search(str,pattern)
print(a)
