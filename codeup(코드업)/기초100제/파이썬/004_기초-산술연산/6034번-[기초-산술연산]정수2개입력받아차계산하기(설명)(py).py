# 코드업 100제 
# 6034번-[기초-산술연산]정수2개입력받아차계산하기(설명)(py).py

'''

정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

예시
...
c = a - b
print(c)

입력
2개의 정수가 공백으로 구분되어 입력된다.

출력
첫 번째 정수에서 두 번째 정수를 뺀 차를 출력한다.

입력 예시
123 -123

출력 예시
246

'''

val1, val2 = input().split()

val1 = int(val1); val2 = int(val2)

print(val1 - val2)

'''

*** 참고
수 - 수는 차(subtraction)가 계산된다.

'''