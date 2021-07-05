def solution(n):
    for i in range(n):
        spaces = (n - i - 1) * " "
        stars = ((i + 1) * "* ").strip()
        print(f"{spaces}{stars}")
    for i in range(n - 2, -1, -1):
        spaces = (n - i - 1) * " "
        stars = ((i + 1) * "* ").strip()
        print(f"{spaces}{stars}")


solution(int(input()))
