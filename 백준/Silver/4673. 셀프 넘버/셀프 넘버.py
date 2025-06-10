num = set(range(1, 10001))
not_self_num = set()

for a in range(1, 10001) :
    for b in str(a):
        a = a + int(b)
    not_self_num.add(a)

self_num = num - not_self_num

for i in sorted(self_num) :
    print(i)
