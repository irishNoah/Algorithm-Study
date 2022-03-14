# 프로그래머스 LV1 - 가운데 글자 가져오기(다른 사람의 풀이)
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12903

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

'''
다른 분의 코드를 참고하여 풀어도 봤다.
보통 나같은 경우는 이러한 문제를 봤을 때 if-else문으로
문제를 접근하여 해결하고자 하는데,
이 분은 한 라인을 바로 return 해버렸다.
최대한 간결하게 짜고자 하는 노력을 해야겠다고 생각했다.
'''

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))