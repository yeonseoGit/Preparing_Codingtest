N = int(input())
a = list(map(int, input().split()))
MM = max(a)
for i in range(0, len(a)):
    a[i] = (a[i]/MM)*100

print(sum(a)/len(a))
