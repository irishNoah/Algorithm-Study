# [현대소프티어]-파이썬-(8단변속기)-LV2-(1-내풀이-성공)-정렬.py
# https://softeer.ai/practice/info.do?idx=1&eid=408

import sys

arr = list(map(int, input().split()))

arrCopy = arr
arrAsc = sorted(arrCopy, reverse=False)
arrDesc = sorted(arrCopy, reverse=True)

if arr == arrAsc:
    print("ascending")
elif arr == arrDesc:
    print("descending")
else:
    print("mixed")