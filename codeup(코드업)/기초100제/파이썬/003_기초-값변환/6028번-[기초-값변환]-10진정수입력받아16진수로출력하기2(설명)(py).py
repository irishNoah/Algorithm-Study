# 코드업 100제 
# 6028번-[기초-값변환]-10진정수입력받아16진수로출력하기2(설명)(py).py

'''

10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

예시
print('%X' % n)  #n에 저장되어있는 값을 16진수 대문자 형태 문자열로 출력

입력
10진수 1개가 입력된다.

출력
16진수(소문자) 형태로 출력한다.

입력 예시
255

출력 예시
FF

'''

val1 = int(input())

print('%X'%val1)

'''
참고

10진수 형태로 입력받고
%X로 출력하면 16진수(hexadecimal)대문자로 출력된다.

16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 A B C D E F)의 문자를 사용한다.
16진수 A는 10진수의 10, B는 11, C는 12 ... 와 같다.

'''