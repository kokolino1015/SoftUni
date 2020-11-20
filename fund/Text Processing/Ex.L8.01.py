words = input().split(", ")
check = allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")
for word in words:
    validation = set(word)
    if 3 < len(word) < 16:
        if validation.issubset(check):
            print(word)
