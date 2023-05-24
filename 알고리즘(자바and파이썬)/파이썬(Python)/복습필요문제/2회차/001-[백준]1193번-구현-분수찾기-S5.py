# [백준]1193번-구현-(분수찾기)-S5-(복습)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1193

n = int(input())
line = 1

# n <= line 이 될 때까지 while문 반봊ㄱ
while n > line:
    n -= line # 이렇게 하면, 각 라인에서 몇 번째 값을 구하려고 하는지 파악할 수 있지
    line += 1

if line % 2 == 0:
    up = n
    down = line - n + 1
else:
    up = line - n + 1
    down = n

print(up,'/',down, sep="")
