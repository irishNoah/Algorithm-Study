# 프로그래머스 LV2 - JadenCase 문자열 만들기
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12951

# 정확성 테스트의 케이스 18개 중 18개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(s):
    answer = ''

    # s의 구성 문자 중 띄어쓰기(' ')를 만났을 때 체크 비트로 사용할 변수 check_null
    # check_null을 사용하는 이유는 공백 이후에 있는 문자가 소문자일 경우 대문자로 변환해야 해주기 때문이다.
    check_null = 0

    # for문을 이용해서 s의 각 구성 문자에 접근
    for i in range(0, len(s)):
        
        # 띄어쓰기(' ')를 만났을 때 answer에 ' '를 더해주고, check_null은 0을 초기화
        if s[i] == ' ':
            answer += s[i]
            check_null = 0

        # check_null이 0이고 s의 요소가 알파벳이 아닐 경우(예 : 숫자)
        # s의 요소를 answer에 더해주고, check_null에 1을 할당
        elif check_null == 0 and s[i].isalpha() == 0:
            answer += s[i]
            check_null = 1

        # check_null이 0이고 s의 요소가 알파벳일 경우
        # s의 요소를 대문자로 변경한 후 answer에 더해주고, check_null에 1을 할당
        elif check_null == 0 and s[i].isalpha() == 1:
            answer += s[i].upper()
            check_null = 1

        # 그 외의 경우에는 s의 구성 요소를 소문자로 변경한 후 answer에 더해줌
        else :
            answer += s[i].lower()

    return answer

s = "3people unFollowed me"	
print(solution(s)) # 결과 예 : "3people Unfollowed Me"