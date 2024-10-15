def solution(progresses, speeds):
    cnt = []
    answer = []
    ssum = 1  # 첫 번째 배포 그룹에는 1개의 작업이 포함됨
    for i in range(0, len(progresses)):
        for j in range(1, 101):  # 최대 100일까지 반복
            if progresses[i] + speeds[i] * j >= 100:
                cnt.append(j)
                break

    M = cnt[0]  # 첫 번째 작업 완료 날짜 기준 설정
    for k in range(1, len(cnt)):
        if cnt[k] <= M:  # 같은 배포 그룹에 포함될 경우
            ssum += 1
        else:  # 새로운 배포 그룹 시작
            answer.append(ssum)  # 이전 배포 그룹의 작업 수 저장
            ssum = 1  # 새로운 배포 그룹이므로 1로 초기화
            M = cnt[k]  # 새로운 배포 기준일 갱신

    answer.append(ssum)  # 마지막 배포 그룹의 작업 수 저장
    return answer

'''def solution(progresses, speeds):
    cnt = []
    answer = []
    ssum = 1
    for i in range(0, len(progresses)):
        for j in range(1, 101):
            if progresses[i]+speeds[i]*j > 100:
                cnt.append(j-1)
                break
    M = cnt[0]
    for k in range(1, len(cnt)):
        if cnt[k] <= M :
            ssum = ssum+1
        else :
            answer.append(ssum)
            ssum = 1
            M =  cnt[k]
    answer.append(ssum)
    return answer'''