# 프로그래머스 LV1 - 시저 암호
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12926

# 정확성 테스트의 케이스 13개 중 13개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(s, n):
    answer = []
    arr = list(s) # 배열 형태로 바꿔주기

    for i in arr:
        # 공백인 것은 그냥 바로 할당
        if i == ' ':
            answer.append(chr(ord(i)))

        # 소문자 또는 대문자일 경우 아래 else문 실행
        else:
            # 대문자일 경우
            if i.isupper() == 1:
                # Z의 아스키 코드가 90인데, n을 밀었을 때 90을 초과할 경우 아래 if 또는 else문 실행
                if ord(i) + n > 90:
                    answer.append(chr(ord(i) + n - 26))
                else:
                    answer.append(chr(ord(i) + n))

            # 소문자일 경우
            else:
                # z의 아스키 코드가 90인데, n을 밀었을 때 122를 초과할 경우 아래 if 또는 else문 실행
                if ord(i) + n > 122:
                    answer.append(chr(ord(i) + n - 26))  
                else:
                    answer.append(chr(ord(i) + n))  

    return "".join(answer)

s = "AaZz"
n = 25
print (solution(s,n))
