# 코드업 100제 
# 6070번-[기초-조건선택실행구조]월입력받아계절출력하기(설명)(py).py

'''

월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

*****예시
-

*****입력
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

*****출력
계절 이름을 출력한다.

*****입력 예시
12

*****출력 예시
winter

'''
# 풀이법 

value = int(input())

if value==12 or value==1 or value==2:
    print("winter")
if value==3 or value==4 or value==5:
    print("spring")
if value==6 or value==7 or value==8:
    print("summer")
if value==9 or value==10 or value==11:
    print("fall")

'''

***** 참고
...
if n//3==1 :
  print("spring")
...

때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

'''