from collections import deque

green_duration = int(input())
free_window_time = int(input())
END_COMMAND = 'END'
GREEN_COMMAND = 'green'

queue_cars = deque()
passed_cars = []

flag = False
car_hit = ''
while True:
    command = input()
    if command == END_COMMAND:
        break
    elif command == GREEN_COMMAND:
        i = 0
        while i < green_duration:
            if queue_cars:
                current_car = queue_cars.popleft()
                if len(current_car) > green_duration - i:
                    queue_cars.appendleft(current_car[green_duration - i:])
                    flag = True
                    car_hit = current_car
                    break
                else:
                    i += len(current_car)
                    passed_cars.append(current_car)
            else:
                break

        i = 0
        if flag:
            current_car = queue_cars.popleft()
            if free_window_time < len(current_car):
                print('A crash happened!')
                print(f'{car_hit} was hit at {current_car[free_window_time - i]}.')
                exit()
            else:
                flag = False
                passed_cars.append(car_hit)
                break
    else:
        queue_cars.append(command)

print('Everyone is safe.')
print(f'{len(passed_cars)} total cars passed the crossroads.')
