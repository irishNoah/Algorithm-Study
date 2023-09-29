# [프로그래머스]-파이썬-연습문제(Lv2)-PCCP 모의고사-(체육대회)-(1-내풀이-실패)-30점.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/15008/lessons/121684

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 22분 소요] / 총 풀이 시간[총 62분 소요]
- 코드 설명 참고할 것

*** 참고

'''
#===================================================================================

def solution(ability):
    print("=" * 50)
    answer = 0

    cnt = 0; flag = False; cmp = []

    # 열 우선순위
    while flag != True:
        arr = [x for x in range(len(ability))]
        count = 0

        for j in range(len(ability[0])):
            # ability의 세로열 값 추출
            col = [sero[j] for sero in ability]
            # 이전에 구해진 행 값은 건너 뛰기 >> 이게 존재하는 값 중 최대값을 구해야 하는 것
            find = []
            for i in range(len(arr)):
                if arr[i] != -1:
                    find.append(col[i])

            # find에서 최대값 구하기
            maxSport = max(find)
            # 최대값에 해당하는 행 위치 구하기
            pRow = col.index(maxSport)
            # 값 차례대로 더해주기
            count += maxSport
            # 최대값 위취에 -100 할당해서 다음 번 계산해서 신경 안쓰게 하기
            ability[pRow][j] = -100
            # 이것도 마찬가지
            arr[pRow] = -1
            print("arr = ", arr)

        cmp.append(count)

        # cnt 값 1 증가
        cnt += 1

        if cnt == len(ability):
            flag = True
            answer = max(cmp)
            break

    return answer

#===================================================================================

# 예제 1
ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability)) # 210

# 예제 2
ability = [[20, 30], [30, 20], [20, 30]]
print(solution(ability)) # 60

# def solution(ability):
#     answer = 0
#     return answer