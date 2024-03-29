# 코드업 100제 
# 6029번-[기초-값변환]-16진정수입력받아8진수로출력하기2(설명)(py).py

'''

16진수를 입력받아 8진수(octal)로 출력해보자.

예시
a = input()
n = int(a, 16)   # 입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  # n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

입력
16진 정수 1개가 입력된다.

출력
8진수 형태로 출력한다.

입력 예시
f

출력 예시
17

'''

val = input()
hexVal = int(val, 16)

print('%o'%hexVal)

'''
*** 참고1

8진법은 한 자리에 8개(0 1 2 3 4 5 6 7)의 문자를 사용한다.
8진수 10은 10진수의 8, 11은 9, 12는 10 ... 와 같다.

*** 참고2

int(x,base=10)

숫자나 문자열 x 로 부터 만들어진 정수 객체를 돌려줍니다.
인자가 주어지지 않으면 0 을 돌려줍니다.
base는 진법을 나타내며 주로 2, 8, 10, 16을 사용합니다. 10이 기본값입니다.

'''