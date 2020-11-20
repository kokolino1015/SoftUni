numbers = input().split(", ")


def palindrome(numbers):
    counter = 0
    n = 0
    for i in numbers:
        counter += 1
    for i in numbers:
        n += 1
        f = []
        s = []
        for j in i:
            f.append(j)
            s.append(j)
        f[0], f[-1] = f[-1], f[0]
        if f == s:
            if n == counter:
                return "True"
            print("True")
        else:
            if n == counter:
                return "False"
            print("False")


print(palindrome(numbers))
