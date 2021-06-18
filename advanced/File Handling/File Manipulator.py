import os


def create(file_name):
    with open(file_name, 'w') as file:
        file.write("")


def add(file_name, content):
    if os.path.exists(file_name):
        with open(file_name, 'a') as file:
            file.write(f'{content}\n')
    else:
        create(file_name)
        with open(file_name, 'a') as file:
            file.write(f'{content}\n')


def replace(file_name, old_string, new_string):
    if not os.path.exists(file_name):
        print('An error occurred')
    else:
        with open(file_name) as file:
            text = file.readlines()
            for i in range(len(text)):
                if old_string in text[i]:
                    text[i] = text[i].replace(old_string, new_string)
            with open(file_name, 'w') as new_file:
                new_file.write(''.join(text))


def delete(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print('An error occurred')


command = input().split('-')

while command[0] != "End":
    if command[0] == 'Create':
        create(command[1])
    elif command[0] == 'Add':
        add(command[1], command[2])
    elif command[0] == 'Replace':
        replace(command[1], command[2], command[3])
    elif command[0] == 'Delete':
        delete(command[1])
    command = input().split('-')
