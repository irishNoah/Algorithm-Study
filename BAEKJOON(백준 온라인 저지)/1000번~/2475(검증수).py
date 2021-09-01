# 2475 / 검증수 / B5
# https://www.acmicpc.net/problem/2475

# 제곱 함수인 pow()를 쓰기 위해 math 라이브러리를 import
import math

# 5개의 고유번호를 공백으로 구분하여 입력하기
numList = list(map(int, input().split()))

# numList 길이가 5와 같지 않다면 no 출력
if len(numList) != 5 :
    print("no")

# 합계 변수 sum 선언 후 0으로 초기화
sum = 0

for i in range(0, len(numList)) :
    # 각 고유번호에 대한 제곱한 수를 sum에 합산
   sum += math.pow(numList[i], 2)

# 검증수 구하기
checkNum = int(sum % 10)

# 검증수 출력하기
print(checkNum)