counties = input().split(", ")
capitals = input().split(", ")

print(*[f"{counties[i]} -> {capitals[i]}" for i in range(len(capitals))], sep="\n")
