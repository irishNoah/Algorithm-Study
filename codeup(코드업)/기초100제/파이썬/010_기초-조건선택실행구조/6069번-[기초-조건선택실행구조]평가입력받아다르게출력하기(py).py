# 코드업 100제 
# 6069번-[기초-조건선택실행구조]평가 입력받아 다르게 출력하기(py).py

'''

평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

*****예시
-

*****입력
영문자 1개가 입력된다.
(A, B, C, D 등 문자 1개가 입력된다.)

*****출력
문자에 따라 다른 내용이 출력된다.

*****입력 예시
A

*****출력 예시
best!!!

'''
# 풀이법 

value = input()

if value=="A":
    print("best!!!")
elif value=="B":
    print("good!!")
elif value=="C":
    print("run!")
elif value=="D":
    print("slowly~")
else:
    print("what?")

'''

***** 참고
-

'''