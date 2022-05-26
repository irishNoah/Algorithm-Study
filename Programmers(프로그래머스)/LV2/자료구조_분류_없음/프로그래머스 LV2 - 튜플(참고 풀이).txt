# 프로그래머스 LV2 - 튜플(참고 풀이)
# https://programmers.co.kr/learn/courses/30/lessons/64065

# 정확성 테스트의 케이스 15개 중 15개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(s):
    answer = []

    # s가 "{{4,2,3},{3},{2,3,4,1},{2,3}}"라고 가정할 때
    # s1은 ['4,2,3', '3', '2,3,4,1', '2,3']가 됨
    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    # 아래 for문을 실행하면 new_s의 결과는 아래와 같음
    # [['4', '2', '3'], ['3'], ['2', '3', '4', '1'], ['2', '3']]
    for i in s1:
        new_s.append(i.split(','))

    # new_s의 내부 리스트의 길이 순서대로 정렬
    new_s.sort(key = len)

    # new_s의 각 리스트 내부의 요소가 answer의 리스트의 요소에 없으면
    # 이 요소를 answer에 append
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    # answer 리턴
    return answer

# 입력
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))