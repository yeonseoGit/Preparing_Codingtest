test = []
not_test = []

for i in range(0, 28) : 
    N = int(input())
    test.append(N)
    test.sort()

for j in range(1, 31):
    if j not in test :
        not_test.append(j)
        test.sort()

for k in range(0, 2):
    print(not_test[k])