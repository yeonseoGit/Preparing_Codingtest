def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] == '-':
        graph[x][y] = 1
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
 
def long(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] == '|':
        graph[x][y] = 1
        long(x+1,y)
        long(x-1,y)
        return True
    return False
 
n,m = map(int,input().split())
graph = [ list(input()) for i in range(n) ]
count = 0
 
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
        if long(i,j) == True:
            count += 1
print(count)