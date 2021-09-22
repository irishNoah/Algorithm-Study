# 1463 / 1로 만들기 / S3
# https://www.acmicpc.net/problem/1463
# 참고 : https://infinitt.tistory.com/247

# 내가 기존에 푼 코드는 
# 주어진 문제에 맞게 풀기는 했지만 단순히 if문으로 푸는 것이 아닌,
# 다이나믹 프로그램으로 풀어야만 하는 듯 하다.
# (내가 기존에 푼 코드는 밑에 있음)

# 정수 입력
n = int(input())
 
# 동적 프로그래밍을 활용하기 위해 리스트 생성
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    # 1을 빼주었을 때 해당
    # 1을 빼기만 하면 이전 횟수에 비해 1회가 추가되는 것이 끝이기 때문이다.
    dp[i] = dp[i-1] + 1

    if i % 3 == 0: # i가 3으로 나누어진다면
        # 기존 dp[i]와 dp[i//3]과 비교를 해준다.
        # 뒤에 +1이 있는 경우에는 이것 역시 이전 횟수에 비해 1값을 추가해주기 때문이다.
        dp[i] = min(dp[i], dp[i//3]+1)
    
    if i % 2 == 0: # i가 2로 나누어진다면
        # 기존 dp[i]와 dp[i//2]과 비교를 해준다.
        # 뒤에 +1이 있는 경우에는 이것 역시 이전 횟수에 비해 1값을 추가해주기 때문이다.
        dp[i] = min(dp[i], dp[i//2]+1)

    if i == 1:
        break

# 횟수 출력
print(dp[n])

################################################################
# # 기존에 내가 푼 코드

# # 정수 값 입력
# n = int(input())

# # 연산을 하는 횟수에 대한 변수 cnt 선언 및 cnt를 0으로 초기화
# cnt = 0

# while True :
#     if n % 3 == 0 : # n을 3으로 나눈 나머지가 0이라면
#         n = int(n/3) # n에다가 기존 n 값을 3으로 나눈 값 대입
#         cnt += 1 # cnt 값 1 증가

#     elif n % 3 == 1 : # n을 3으로 나눈 나머지가 0이 아니라면
#         # 일단 n_CVT라는 변수에 n-1 값을 대입
#         n = n - 1 

#         n = int(n/3) # n에다가 기존 n 값을 3으로 나눈 값 대입

#         cnt += 2 # cnt 값 1 증가
        
#     elif n % 3 == 2 :
#         n = int(n / 2)
#         cnt += 1

#     if n == 1 :
#         break

# print(cnt)