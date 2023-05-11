# 코드업 100제 
# 6058번-[기초-논리연산]둘다거짓일경우만참출력하기(py).py

'''

2개의 정수값이 입력될 때,
그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

예시
-

입력
2개의 정수가 공백을 두고 입력된다.

출력
두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.

입력 예시
0 0

출력 예시
True

'''
# 풀이법 

a, b = input().split()

print(not (bool(int (a)) or bool(int (b))))


'''

*** 참고
-

'''