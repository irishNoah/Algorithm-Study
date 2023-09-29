# [프로그래머스]-파이썬-힙-(기말고사)-(1-내풀이-IDE정답+시간초과많아)-29점.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- val = sys.maxsize
- 최대 과목 수에 대한 변수 point
- k(구할 수 있는 기출문제 수)가 0이 아닐 때까지
    - pstudy에서 가장 작은 값(= cnt)을 선택한다.
        - 만약, 이 값이 t보다 작거나 같다면
            - t = t - cnt
            - k = k-1
            - point += 1
            - study[i]와 pstudy[i]의 값에 val을 넣어줌 > 인덱스로 찾아줘
                - 얘네들은 이제 더이상 신경 써주면 안되니까
        - 만약, 이 값이 t보다 크다면
            - 더이상, 계산할 수 없으므로 point를 리턴한다.
                - 어차피 study의 값이 pstudy보다 크니깐!
- k가 0이 됐지만, t가 남아 있다면 > t(보유 시간)가 0 미만이 아닐 때까지
    - study에서 가장 작은 값(= cnt)을 선택한다.
        - 만약, 이 값이 t보다 작거나 같다면
            - t = t - cnt
            - point += 1
            - study[i]의 값에 val을 넣어줌 > 인덱스로 찾아줘
                - 얘네들은 이제 더이상 신경 써주면 안되니까
        - 만약, 이 값이 t보다 크다면
            - 더이상, 계산할 수 없으므로 point를 리턴한다.

*** 참고

'''
#===================================================================================
import sys

def solution(t, k, study, pstudy):
    # print("=" * 50)
    val = sys.maxsize  # 9223372036854775807
    point = 0 # 최대 과목 수

    while k != 0 :
        cnt = min(pstudy)
        if cnt <= t:
            t = t - cnt
            k -= 1
            point += 1
            idx = pstudy.index(cnt) # 인덱스 값 찾기
            study[idx] = val; pstudy[idx] = val

        if cnt > t:
            return point

    # print("study = ", study)
    # print("pstudy = ", pstudy)
    # print("now point = ", point)
    # print("left time = ", t)
    # print("@" * 50)

    while t >= 0:
        cnt = min(study)
        if cnt <= t:
            t = t-cnt
            point += 1
            idx = study.index(cnt) # 인덱스 값 찾기
            study[idx] = val

        if cnt > t:
            return point

    # return point
#===================================================================================

# 예제 1
t = 10
k = 2
study = [8,13,8,9,5]
pstudy = [1,3,4,7,4]
print(solution(t, k, study, pstudy)) # 3

# 예제 2
t = 100
k = 3
study = [90,100,90,80,40,50]
pstudy = [1,2,3,10,20,30]
print(solution(t, k, study, pstudy)) # 4


# def solution(t, k, study, pstudy):
#     answer = 0
#     return answer