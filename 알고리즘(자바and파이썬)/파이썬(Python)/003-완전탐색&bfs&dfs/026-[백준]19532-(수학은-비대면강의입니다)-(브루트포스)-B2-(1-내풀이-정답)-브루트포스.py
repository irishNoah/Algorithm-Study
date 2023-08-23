# [백준]19532-(수학은-비대면강의입니다)-(브루트포스)-B2-(1-내풀이-정답)-브루트포스.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/19532

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)

*** 조건

*** 설계 [총 1분 소요] / 총 풀이 시간[총 -분 소요]

*** 참고

'''
#===================================================================================
import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)

#===================================================================================