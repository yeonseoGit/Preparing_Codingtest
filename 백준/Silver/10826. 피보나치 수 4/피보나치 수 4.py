n = int(input())
a, b = 0, 1 

for _ in range(2, n + 1):  
    a, b = b, a + b  

print(b if n > 0 else a)  