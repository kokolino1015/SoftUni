number = int(input())


def loading_bar(number):
    d = number // 10
    if number == 100:
        print("100% Complete!")
        return "[%%%%%%%%%%]"
    else:
        if number in range(0, 11):
            print(f"{number}% [%.........]")
        elif number in range(10, 21):
            print(f"{number}% [%%........]")
        elif number in range(20, 31):
            print(f"{number}% [%%%.......]")
        elif number in range(30, 41):
            print(f"{number}% [%%%%......]")
        elif number in range(40, 51):
            print(f"{number}% [%%%%%.....]")
        elif number in range(50, 61):
            print(f"{number}% [%%%%%%....]")
        elif number in range(60, 71):
            print(f"{number}% [%%%%%%%...]")
        elif number in range(70, 81):
            print(f"{number}% [%%%%%%%%..]")
        elif number in range(80, 91):
            print(f"{number}% [%%%%%%%%%.]")
        return "Still loading..."


print(loading_bar(number))
