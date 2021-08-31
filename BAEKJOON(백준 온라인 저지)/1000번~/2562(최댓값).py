# 2562 / 최댓값 / B2
# https://www.acmicpc.net/problem/2562

# 최대값을 찾기 위한 list인 findMax 선언
findMax = []

# 9개의 값 입력받기
for i in range(0, 9) :
    value = int(input())
    findMax.append(value)

# 리스트의 길이가 9가 아니면 틀렸다고 출력해주기
if len(findMax) != 9 :
    print("no")

# maxValue에 findMax 리스트 요소 중 가장 큰 값을 max() 함수를 통해 찾고 대입해주기
maxValue = max(findMax)
# 최대값 출력
print(maxValue)

# index라는 변수에서 findMax 중 최대값에 해당되는 인덱스를
# index()라는 함수를 통해 찾고 대입해주기
index = findMax.index(maxValue)
# 문제에서는 실제 인덱스보다 1을 더해준 값을 요구하고 있으므로
# 기존 index 값에 1을 더해준 값을 대입
index = index+1
# index 출력
print(index)