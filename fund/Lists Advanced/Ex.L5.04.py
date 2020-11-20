rooms = int(input())
needed_chairs = 0
left = 0
for room in range(1, rooms + 1, 1):
    places = input().split(" ")
    if len(places[0]) < int(places[1]):
        needed = int(places[1]) - len(places[0])
        needed_chairs += needed
        print(f"{needed} more chairs needed in room {room}")
    elif len(places[0]) > int(places[1]):
        left_chairs = len(places[0]) - int(places[1])
        left += left_chairs
if needed_chairs == 0:
    print(f"Game On, {left} free chairs left")