#given an interger array,output all th unique pars that sum up to specific value k
#using set -O(n)


def pairsum(arr,k):
    if len(arr) < 2:
        return

    #sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num,target),max(num,target))))

    #return len(output)
    print("'\n'".join(map(str,list(output))))

#print(pairsum([1,3,2,2],4))
pairsum([1,3,2,2],4)
