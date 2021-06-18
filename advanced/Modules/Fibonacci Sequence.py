import fibonacci

sequence = []
command = input().split(' ')
while command[0] != "Stop":
    if command[0] == 'Create':
        sequence = fibonacci.create_sequence(int(command[2]))
        print(' '.join(str(x) for x in sequence))
    elif command[0] == 'Locate':
        find = fibonacci.locate(sequence, int(command[1]))
        print(find)

    command = input().split(" ")
