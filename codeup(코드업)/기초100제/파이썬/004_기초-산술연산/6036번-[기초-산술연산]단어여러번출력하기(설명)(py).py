# 코드업 100제 
# 6036번-[기초-산술연산]단어여러번출력하기(설명)(py).py

'''

단어와 반복 횟수를 입력받아 여러 번 출력해보자.

예시
w, n = input().split()
print(w*int(n))

입력
단어와 반복 횟수가 공백으로 구분되어 입력된다.

출력
입력된 단어를 입력된 횟수만큼 반복해 출력한다.

입력 예시
love 3

출력 예시
lovelovelove

'''

val1, val2 = input().split()

print(val1 * int(val2))

'''

*** 참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.

'''