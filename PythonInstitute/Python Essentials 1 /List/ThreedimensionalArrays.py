import random as rd

a = rd.randint(0, 1)


rooms = [[[rd.randint(0, 1) for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True

rooms[2][14][13] = True

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(rooms)

print(vacancy)
