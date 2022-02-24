# 프로그래머스 LV2 - 최댓값과 최솟값
# https://programmers.co.kr/learn/courses/30/lessons/12939

# 정확성 테스트의 케이스 12개 중 12개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(s):
    # 리스트 s를 공백으로 구분하여 리스트 answer에 대입
    answer = s.split()

    # 숫자 오름차순 식으로 문자열 숫자 정렬하기
    answer.sort(key = int)

    # 최솟값과 최댓값 return하기
    return str(answer[0]) + " " + str(answer[-1])

s = "-1 -1"
print(solution(s))