import sys
from collections import deque
import ast

input = sys.stdin.readline

t = int(input())  # 테스트케이스 개수

for _ in range(t):
    commands = input().strip()  # 함수 문자열 ex) "RDD"
    n = int(input())  # 배열 길이
    arr_str = input().strip()  # 배열 입력 ex) "[1,2,3,4]"

    # 빈 배열일 경우 예외 처리
    if arr_str == "[]":
        arr = deque()
    else:
        arr = deque(ast.literal_eval(arr_str))  # 문자열을 진짜 리스트로 바꾸고 deque로 감싸기

    is_reversed = False  # 뒤집힘 여부 표시
    error = False  # 에러 여부 표시

    for cmd in commands:
        if cmd == 'R':
            is_reversed = not is_reversed  # R이 나올 때마다 방향 뒤집기
        elif cmd == 'D':
            if not arr:
                error = True
                break  # 빈 배열에서 삭제 시도 → 에러
            if is_reversed:
                arr.pop()  # 뒤집힌 상태면 오른쪽에서 제거
            else:
                arr.popleft()  # 일반 상태면 왼쪽에서 제거

    if error:
        print("error")
    else:
        if is_reversed:
            arr.reverse()  # 최종 출력 전에 실제로 뒤집기
        print("[" + ",".join(map(str, arr)) + "]")  # 형식에 맞게 출력
