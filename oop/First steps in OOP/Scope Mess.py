x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"
        return x

    print("outer:", x)
    inner()
    print("outer:", x)
    x = change_global()
    return x


print(x)
x = outer()
print(x)
