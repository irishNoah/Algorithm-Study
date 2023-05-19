# [백준]11399번-그리디-ATM-S4
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/11399

n = int(input())

time = input().split() # 리스트 입력

time = list(map(int, time)) # 리스트 내부 요소 정수화

time.sort()

sumTime = 0 # i-1번째 까지 사람까지 걸린 시간과 i번째 사람의 time을 더하기 위한 값
result = 0 # 최종 결과값

for i in range(0, n): # 내 풀이
    sumTime += time[i]
    result += sumTime

print(result)

# --------------------------------------------------
# 다른 분 풀이

answer = 0

for x in range(1, n+1): 
    answer += sum(time[0:x])

print(answer)