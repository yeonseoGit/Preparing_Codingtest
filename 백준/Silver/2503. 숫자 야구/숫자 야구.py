import sys
input = sys.stdin.readline

n = int(input())

que = [list(map(int, input().split())) for _ in range(n)]

candidates = []
for num in range(123, 988):
    num_str = str(num)
    if '0' in num_str:
        continue
    if len(set(num_str)) != 3:
        continue
    candidates.append(num_str)

result = 0

for nums in candidates :
    possible = True

    for a, s, b in que :
        s_cnt = 0
        b_cnt = 0
        m_a = list(str(a))
        for i in range(3):
            if nums[i] == m_a[i]:
                s_cnt += 1
        for i in range(3):
            if (nums[i] != m_a[i]) and (nums[i] in m_a) :
                b_cnt += 1
        
        if s_cnt != s or b_cnt != b :
            possible = False
            break
    
    if possible :
        result += 1

print(result)
