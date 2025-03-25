a = list(map(int, input().split()))

for i in range(0, 7):
    if a[i+1] == a[i]+1:
        result = 'ascending'
    elif a[i+1] == a[i]-1:
        result = 'descending'
    else :
        result = 'mixed'
        break

print(result)