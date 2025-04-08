'''
 현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나, 
 포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 하도록
'''
import sys

Input = sys.stdin.readline

N, M = map(int, Input().split())

pocket = {}
reserve = {}

for i in range(N):
    name = Input().strip()
    pocket[name] = i+1
    reserve[str(i+1)] = name

for _ in range(M):
    monster = Input().strip()
    if monster.isdigit():
        print(reserve[monster])
    else:
        print(pocket[monster])