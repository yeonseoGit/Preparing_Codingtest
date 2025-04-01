import sys
input = sys.stdin.readline

N = int(input())
nn = set(map(int, input().split()))

M = int(input())
mm = list(map(int, input().split()))

for num in mm:
    print(1 if num in nn else 0)
