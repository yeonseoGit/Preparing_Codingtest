from collections import defaultdict
import sys

input = sys.stdin.readline

def max_fruit_tanghuru_length(N, fruits):
    count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(N):
        count[fruits[right]] += 1

        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

N = int(input())
fruits = list(map(int, input().split()))
print(max_fruit_tanghuru_length(N, fruits))
