import sys
input = sys.stdin.readline

n = int(input())

x_ori = list(map(int, input().split()))
x_sort = sorted(list(set(x_ori)))

value_to_index = dict()
for idx in range(len(x_sort)):
    value = x_sort[idx]
    value_to_index[value] = idx

result = []
for x in x_ori:
    result.append(value_to_index[x])


print(*result)