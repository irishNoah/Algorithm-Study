# 2609 / 최대공약수와 최소공배수 / S5
# https://www.acmicpc.net/problem/2609

# 최대 공약수와 최소 공배수 함수를 사용하기 위해
# math 라이브러리를 import 해주기
import math

# 2개의 변수에 숫자 입력 받기
a, b = map(int, input().split())

# 최대 공약수를 구하기 위해 gcd() 함수를 사용
gcd = math.gcd(a, b)

# 최소 공배수를 구하기 위해 lcm() 함수를 사용
lcm = math.lcm(a, b)

# 최대 공약수 및 최소 공배수 출력
print(gcd)
print(lcm)