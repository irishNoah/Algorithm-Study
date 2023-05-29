# [백준]1193번-파이썬-구현-(분수찾기)-S5-(2-복습)-성공.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1193

'''

'''

val = int(input())
line = 1

while True:
    if val > line:
        val = val-line
        line += 1

    else :
        break

bunmo = 0; bunja = 0

if line % 2 == 1:
    bunmo = val
    bunja = line+1-val
else:
    bunmo = line+1-val
    bunja = val

print("{0}/{1}".format(bunja, bunmo))