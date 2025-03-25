bin = list(map(int, input().split()))

for i in range(0, 5) :
    bin[i] = bin[i]*bin[i]

result = sum(bin)%10
print(result)