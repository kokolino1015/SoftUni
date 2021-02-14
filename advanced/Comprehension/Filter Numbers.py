def read_matrix():
    start = int(input())
    end = int(input())
    return [num for num in range(start, end + 1)], [num for num in range(2, 11)]


matrix, two_to_ten_matrix = read_matrix()

print([num for num in matrix if any(num % x == 0 for x in two_to_ten_matrix)])
