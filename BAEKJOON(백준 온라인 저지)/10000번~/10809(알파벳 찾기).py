# 10809 / 알파벳 찾기 / B2
# https://www.acmicpc.net/problem/10809

# 단어 입력
word = input()

# a~z까지 소문자의 개수는 총 26개이다.
for i in range(26) :
    # find() 함수
    # 윗 함수는 문자열에 대해 찾고자하는 값을 넣어줄 경우 
    # 그 값의 index 위치를 찾아주는 함수이다.
    # 참고로, 한 단어 또는 문자열 안에서 동일한 값이 여러개라고 한다고 하더라도
    # 맨 처음에 나온 값에 대한 위치만 반환해준다.
    # 또한 찾고자 하는 값이 단어 또는 문자열에 없을 경우 -1을 반환한다.
    # ------------------------------------------------------------
    # chr() 함수
    # 윗 함수는 () 안에 아스키코드 값을 기반으로 실제 값을 알 수 있는 함수이다.
    # 예를 들어 소문자 a의 아스키코드는 97인데, chr(97)은 a인셈이다. 
    print(word.find('{0}'.format(chr(97+i))), end=' ')