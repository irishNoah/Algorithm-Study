# 코드업 100제 
# 6052번-[기초-논리연산]정수입력받아참거짓평가하기(설명)(py).py

'''

정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

예시
n = int(input())
print(bool(n))

입력
정수 1개가 입력된다.

출력
입력된 값이 0이면 False, 0이 아니면 True 를 출력한다.

입력 예시
0

출력 예시
False

'''
# 풀이법 

a = int(input())


# 풀이법 1
print(bool(a)) # bool() 정수 0만 False, 나머지들은 다 True

# 풀이법 2
if a == 0:
    print(False)

else:
    print(True)


'''

*** 참고
bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다.
식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다. 

python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다.

** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 
True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.

'''