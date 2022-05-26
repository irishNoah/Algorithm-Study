# 프로그래머스 LV2 - 튜플(내 풀이)
# https://programmers.co.kr/learn/courses/30/lessons/64065

# 정확성 테스트의 케이스 15개 중 15개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

# https://somjang.tistory.com/entry/Python-str-%ED%98%95%EC%8B%9D%EC%9D%98-list-%EB%AC%B8%EC%9E%90%EC%97%B4-list-%ED%98%95%EC%8B%9D%EC%9C%BC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-str-list-to-list-python
# str 형식의 list 문자열 list 형식으로 변환하는 방법(str list to list python)을 하기 위해 ast 라이브러리를 import 해주었다.
# 자세한 설명은 위 링크를 참고할 것
import ast

def solution(s):
    # s는 set 형식의 문자열로 이루어져 있음. 일단 list 형태로 만들어주고자
    # s에 있던 '{', '}'를 각각 '[', ']'으로 변경
    s = s.replace('{', '[')
    s = s.replace('}', ']')

    # 문자열로 이루어진 s를 ast라이브러리를 활용하여 list로 변경
    # 예시 s = '[2]' >>> 이건 문자열 / s = [2] >>> 이건 리스트
    s = ast.literal_eval(s)

    # 2차원 리스트에서 내부 리스트의 길이순으로 정렬
    s.sort(key=len) 

    # 2차원 for를 활용하여 만약 리스트 s 내부 리스트의 각 요소가
    # result에 없는 요소이면 result에 append
    answer = []

    for arr in s:
        for value in arr:
            if value not in answer:
                answer.append(value)

    # 결과 리턴
    return answer

# 입력
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))