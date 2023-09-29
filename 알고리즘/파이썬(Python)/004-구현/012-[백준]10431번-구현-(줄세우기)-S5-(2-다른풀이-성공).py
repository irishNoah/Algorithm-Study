# [백준]10431번-구현-(줄세우기)-S5-(2-다른풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10431

'''
# 문제 풀이

'''

import sys

for _ in range(int(input())):
    a=list(map(int,input().split()))
    case,li=a[0],a[1:]
    cnt=0

    for i in range(1,20):
        for j in range(i):
            if li[i]<li[j]:
                cnt+=1


    print(case,cnt)