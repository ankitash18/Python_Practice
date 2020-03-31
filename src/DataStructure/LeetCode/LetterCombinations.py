def letterCombinations(digits) :
    d = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    output = []
    print(type(output))

    for digit in str(digits):
        print(f"digit.{digit}")
        if not output:
            for x in d[digit]:
                output.append(x)
                print(output)
        else:
            new_output = []
            for i in range(len(output)):
                for letter in d[digit]:
                    new_output.append(output[i] + letter)
                    print(new_output)
                    print(output)
            output = new_output



    return output


a= letterCombinations(234)
print(a)
