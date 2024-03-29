# 코드업 100제 
# 6025번-[기초-값변환]-정수2개입력받아합계산하기(설명)(py).py

'''

정수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

예시
a, b = input().split()
c = int(a) + int(b)
print(c)

입력
2개의 정수가 공백으로 구분되어 입력된다.

출력
두 정수의 합을 출력한다.

입력 예시
123 -123

출력 예시
0

'''

val1, val2 = input().split()

val1 = int(val1)
val2 = int(val2)

print(val1+val2)

'''
참고

입력되는 값은 기본적으로 문자열로 인식된다.

문자열 + 문자열은 두 문자열을 합친 문자열을 만든다.
숫자로 구성된 문자열이나 실수를 정수(integer) 값으로 바꾸기 위해서는 int( ) 를 사용할 수 있다.
수 + 수의 결과는 합(addition)이 계산된다.

'''