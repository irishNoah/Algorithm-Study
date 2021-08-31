# 1934 / 최소공배수 / S5
# https://www.acmicpc.net/problem/1934

# 최대 공약수와 최소 공배수 함수를 사용하기 위해
# math 라이브러리를 import 해주기
import math
import sys

# 테스트 케이스의 개수 입력
testCase = int(input())

for i in range(testCase) :
    command = sys.stdin.readline().split()
    
    command[0] = int(command[0])
    command[1] = int(command[1])
    
    # 두 숫자에 대한 최소공배수를 lcm() 함수를 이용하여 구하기
    lcm = math.lcm(command[0], command[1])
    print(lcm)