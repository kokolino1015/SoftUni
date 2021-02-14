matrix = input().split(", ")

print(*[f"{word} -> {len(word)}" for word in matrix], sep=", ")
