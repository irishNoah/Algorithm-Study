# 11050 / 이항 계수 1 / B1
# https://www.acmicpc.net/problem/11050

# factorial 함수를 사용하기 위해 math 라이브러리 import하기
import math

n, k = map(int, input().split())

nValue= 1
# 이 문제에서는 조합 C를 원하는 것이다.
# 즉 C(n,k)에서 n이 5, k가 2라면
# C(5, 2) = 5*4 / 2*1 이므로
# K의 값이 무엇이냐에 따라 위의 분자의 곱 값이 달라진다.
# 따라서 for문을 통해 분자 값을 구해준다.
for i in range(1, k+1):
    nValue = nValue * n
    n -= 1

# factorial 함수를 통해 분모 값을 구해준다.
kFac = math.factorial(k)

# C(n,k)의 값을 구해준다.
answer = int(nValue / kFac)

print(answer)