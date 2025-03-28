a = -1

while a != 0 :
    N = list(map(int, input()))
    if N[0] == 0 :
        a = 0
        break
    M = list(reversed(N)) # N.reverse()는 안됨.
    if N == M :
        print("yes")
    else :
        print("no")