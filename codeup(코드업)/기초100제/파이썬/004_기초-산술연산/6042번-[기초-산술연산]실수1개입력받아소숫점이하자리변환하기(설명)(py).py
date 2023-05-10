# 코드업 100제 
# 6042번-[기초-산술연산]실수1개입력받아소숫점이하자리변환하기(설명)(py).py

'''

실수 1개를 입력받아
소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

예시

a=input()
a=float(a)
print( format(a, ".2f") )

입력
실수 1개가 입력된다.

출력
소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력한다. 

입력 예시
3.141592

출력 예시
3.14

'''
# 풀이법 

val1 = float(input())

print('%.2f'%val1) # 동일한 결과 출력
print( format(val1, ".2f") ) # 동일한 결과 출력

'''

*** 참고
format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다. 

여기서 만들어진 값은 소수점 아래 3번째 자리에서 반올림한 값이다.

컴퓨터 프로그래밍에서 실수 변환이나 실수를 사용하는 계산은
정확하게 변환되거나 계산되는 것이 아니라, 거의 모두 근사값으로 계산되는 것이라고 할 수 있다. 

실수가 컴퓨터로 저장되기 위해서는 디지털방식으로 2진 정수화되어 저장되어야 하는데,
그 과정에서 아주 작은 부분이 저장되지 않고 사라지는 잘림(truncation) 오차가 자주 발생하기 때문이다.

*** 풀이법
나는 print('%.2f'%val1) 를 활용하여 문제를 해결하였음

아주 잘 한 것 같음

'''