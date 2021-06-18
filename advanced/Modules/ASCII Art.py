import pyfiglet


def print_art(msg):
    ascii_art = pyfiglet.figlet_format(msg)
    return ascii_art


print(print_art(input()))
