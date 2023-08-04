# [현대소프티어]-파이썬-(주행거리-비교하기)-LV1-(내풀이-성공)-if문.py
# https://softeer.ai/practice/info.do?idx=1&eid=1016&sw_prbl_sbms_sn=234482

import sys

a, b = map(int, input().split())

if a > b :
    print("A")

elif a < b:
    print("B")

else:
    print("same")