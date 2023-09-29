# [프로그래머스]-파이썬-그리디-(큰수만들기)-LV2-(1-내풀이-정답)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 10분 소요] / 총 풀이 시간[총 20분 소요]


'''
#===================================================================================

def solution(number, k):
    answer = ''
    number = list(number)
    arr = [] # 스택을 활용하기 위한 리스트

    for i in range(len(number)):
        # k > 0인 상태에서, arr에 쌓여진 수 중 비교할 값보다 작은 게 있다면
        # pop()을 활용해서 제거 작업 진행 and k는 1 감소
        while k > 0 and len(arr) != 0 and arr[-1] < number[i]:
            arr.pop()
            k = k-1

        if k == 0 :
            # k가 0이 됐지만 아직 비교할 것들이 남아있다면,
            # 이것들은 구해진 arr과 합쳐버림
            if i != len(number)-1:
                answer = "".join(map(str, arr)) + "".join(map(str, number[i:]))

            # 비교할 것이 없다면, 끝까지 비교한 것이므로
            # arr과 마지막 값만 더해주면 됨
            else:
                answer = "".join(map(str, arr)) + number[i]
            break

        arr.append(number[i])

    # 만약, k는 2인데 주어진 number가 "98765"나 "93765"와 같이
    # 어느 정도 정렬되어 있는 상태라 k가 0이 될 수 없는 상태라면
    # 위 for문에서 구해진 arr 상태에서 -k 직전까지의 값을 answer에 할당당
    if k != 0:
       answer = "".join(map(str, arr[:-k]))

    return answer

#===================================================================================

# 예제 1
number = "1924"
k = 2
print(solution(number, k)) # "94"

# 예제 2
number = "1231234"
k = 3
print(solution(number, k)) # "3234"

# 예제 3
number = "4177252841"
k = 4
print(solution(number, k)) # "775841"

# 히든 테케
number = "98765"
k = 2
print(solution(number, k)) # "987"

# 히든 테케
number = "93765"
k = 2
print(solution(number, k)) # "976"

# def solution(number, k):
#     answer = ''
#     return answer