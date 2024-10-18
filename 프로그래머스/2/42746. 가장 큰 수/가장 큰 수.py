def solution(numbers):
    maxint=str(max(numbers))
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*len(maxint))
    numbers=numbers[::-1]
    answer=str(int(''.join(numbers)))
    return answer

#numbers=[6,10,2] //예시 확인용
#print(solution(numbers))
