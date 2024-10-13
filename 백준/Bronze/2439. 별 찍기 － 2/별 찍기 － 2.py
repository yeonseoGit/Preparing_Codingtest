star = int(input())
a = ''

for i in range(star, 0, -1):
    a = ' '*(i-1)
    a = a + '*'*(star-i+1)
    print(a)
