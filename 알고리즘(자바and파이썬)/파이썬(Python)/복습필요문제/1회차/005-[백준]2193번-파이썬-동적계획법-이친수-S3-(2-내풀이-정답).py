# [백준]2193번-파이썬-동적계획법-이친수-S3-(2-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2193

'''
n이 1일 때부터 6일 때
각 이진수를 구해보고, 여기서 이친수가 몇 개인지 각각 구해보면
피보나치 수와 동일한 값이 나온다는 것을 알 수 있다.

확실히 코테에서는 구현 문제로 출제하지 않는 이싱
컴퓨터에 무리를 가하지 않는다는 점을 알고 규칙을 발견하는 것이 관건이겠다.
'''

n = int(input())


if n == 1 or n == 2:
    print(1)

else :
    table = [0] * (n + 1)

    table[1] = 1;
    table[2] = 1;
    
    # 이친수 구하기 > 피보나치와 동일
    for i in range(3, n+1):
        table[i] =  table[i-1] + table[i-2]

    print(table[n])