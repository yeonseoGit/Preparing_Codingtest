import sys
input = sys.stdin.readline

words = set(input().strip() for _ in range(int(input())))
for word in sorted(words, key=lambda x: (len(x), x)):
    print(word)
