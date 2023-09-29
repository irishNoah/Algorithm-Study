# [프로그래머스]-파이썬-연습문제-(가장-가까운-같은-글자)-LV1-(2-참고-)-딕셔너리활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
>>> 1 ≤ s의 길이 ≤ 10,000
>>> s은 영어 소문자로만 이루어져 있습니다.

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

'''
#===================================================================================

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            # dic에 있다면 i와 dic에 있는 알파벳 값 뺀 것을 answer에 할당
            answer.append(i - dic[s[i]])

        # 키 : 알파벳 / 값 : 인덱스 위치
        dic[s[i]] = i

    return answer

#===================================================================================

s = "banana"
print(solution(s)) # [-1, -1, -1, 2, 2, 2]

# def solution(s):
#     answer = []
#     return answer