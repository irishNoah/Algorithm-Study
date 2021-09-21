# 1158 / 요세푸스 문제 / S5
# https://www.acmicpc.net/problem/1158

# 총 인원 수 n명과 양의 정수 k 입력
n, k = map(int, input().split())

# 리스트 arr에 1부터 n까지 인원 할당
arr = [i for i in range(1, n+1)]

# pop된 순서를 출력해야 하므로, 출력을 하기 위한 리스트 answer 선언
answer = []

# 원을 도는 주기 num
num = k-1

for i in range(n):
    # 위치(= 한 바퀴를 다 돌았을 경우)가 리스트를 넘지 않은 경우
    # 주기대로 해당하는 인덱스의 값을 제거
    if len(arr) > num:
        answer.append(arr.pop(num))
        num += k-1

    # 위치(= 한 바퀴를 다 돌았을 경우)가 리스트를 넘은 경우
    # 리스트 길이를 주기로 나눈 나머지를 인덱스로 하는 값을 제거
    elif len(arr) <= num:
        num = num % len(arr)
        answer.append(arr.pop(num))
        num += k-1

# 출력
print("<", ', '.join(str(i) for i in answer), ">", sep = '')