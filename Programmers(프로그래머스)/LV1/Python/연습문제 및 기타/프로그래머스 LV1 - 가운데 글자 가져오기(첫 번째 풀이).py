# 프로그래머스 LV1 - 가운데 글자 가져오기(첫 번째 풀이)
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12903

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(s):
    answer = ''
    
    # 문자열의 길이가 홀수일 경우는 아래 if문을 따름
    if len(s) % 2 == 1:
        answer = s[int(len(s) / 2 - 0.5)]

    # 문자열의 길이가 짝수일 때는 아래 else문을 따름
    else : 
        answer = s[int(len(s)/2-1):int(len(s)/2+1)]

    return answer
    
s = "qwer"
print(solution(s)) # 답안 예 : we