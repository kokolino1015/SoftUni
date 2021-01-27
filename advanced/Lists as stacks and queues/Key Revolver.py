from collections import deque

price = int(input())
capacity = int(input())

bullets = deque(input().split(" "))
locks = deque(input().split(" "))
stash = int(input())
bullets_used = 0
current_capacity = capacity

while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        exit()
    current_lock = int(locks.popleft())
    current_bullet = int(bullets.pop())
    if current_bullet <= current_lock:
        print("Bang!")
    elif current_lock < current_bullet:
        print("Ping!")
        locks.appendleft(current_lock)
    bullets_used += 1
    current_capacity -= 1
    if current_capacity == 0 and bullets:
        print("Reloading!")
        current_capacity += capacity

print(f"{len(bullets)} bullets left. Earned ${stash - bullets_used * price}")
