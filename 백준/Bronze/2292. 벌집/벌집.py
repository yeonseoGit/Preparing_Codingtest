N = int(input())

if N == 1:
    print(1)
else:
    NN = N - 1 
    room = 1 
    while NN > 0:
        NN -= 6 * room
        room += 1
    print(room)
