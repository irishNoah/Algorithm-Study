# [백준]2979번-구현-(트럭 주차)-B2-(2-다른풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2979

'''
# 문제 풀이

1. 메모리와 시간 모두 내 풀이와 동일했음
하지만, 코드수가 훨씬 간결하기에 이걸로 연습해도 좋을 듯 
'''

a,b,c = map(int,input().split())
num=[]
for i in range(3):
  In,Out = map(int,input().split())
  for i in range(In+1, Out+1):
    num.append(i)

sum = 0

for i in num:
  if num.count(i)==1:
    sum += a
  elif num.count(i)==2:
    sum += b
  elif num.count(i)==3:
    sum += c
print(sum)