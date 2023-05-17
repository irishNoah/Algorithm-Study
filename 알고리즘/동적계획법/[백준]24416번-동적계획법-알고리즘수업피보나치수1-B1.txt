# [백준]24416번-동적계획법-알고리즘수업피보나치수1-B1
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24416

def fibonacci_dp(val): # dp
    table = [0]*41

    # 리스트 table은 다른 리스트도 마찬가지로 인덱스가 0부터 시작이지만
    # 피보나치 n번째 수와 맞먹게 인덱스를 0이 아닌 1부터 시작하도록 코딩
    table[1] = 1; table[2] = 1 
    
    cnt = 0 # 실행 횟수 - 문제 조건에서 val이 5부터 시작이기 때문에 -1로 초기화

    for i in range(3, val+1):
        cnt += 1
        table[i] = table[i-1] + table[i-2]

    return print(table[val], cnt)
   

val = int(input())
fibonacci_dp(val)