# 1546 / 평균 / B1
# https://www.acmicpc.net/problem/1546

# 시험 본 과목의 개수 n 입력
n = int(input())

# 리스트 변수 test에 각 시험 점수 공백으로 구분하여 입력
test = list(map(int, input().split()))

# test의 길이가 n과 같지 않다면 no 출력
if len(test) != n :
    print("no")

# 합산 변수 sum
sum = 0
# 초기 test 리스트 안의 최댓값을 저장하는 변수 maxValue
maxValue = max(test)

for i in range(0, len(test)) :
    # 각 과목에 대한 점수 주작
    test[i] = test[i] / maxValue * 100
    # 주작한 점수를 sum에 합산
    sum += test[i]

# 주작 점수 총 합산을 과목 수로 나누어 평균 구하기
print(sum / n)