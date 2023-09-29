# [현대소프티어]-파이썬-(A+B)-LV1-(1-내풀이-성공)-for문.py
# https://softeer.ai/practice/info.do?idx=1&eid=362

import sys

case = int(input())

for i in range(1, case+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print("Case #", i, ": ", (a+b), sep="")