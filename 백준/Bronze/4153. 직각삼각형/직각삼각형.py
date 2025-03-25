a = -1
tri = []
while a != 0:
    tri = list(map(int, input().split()))
    if tri[0] == 0 :
        a = 0
        break
    tri.sort()
    if tri[2]**2 == (tri[1]**2 + tri[0]**2) :
        print('right')
    else :
        print('wrong')