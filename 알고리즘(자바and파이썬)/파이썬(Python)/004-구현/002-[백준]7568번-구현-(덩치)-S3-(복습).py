# [백준]7568번-구현-(덩치)-S3-(복습)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/7568

n = int(input())
infor = []

for _ in range(n):
    x, y = map(int, input().split())

    infor.append([x, y])

for i in range(n):
    rank = 1

    for j in range(n):
        if infor[j][0] > infor[i][0] and infor[j][1] > infor[i][1]:
            rank += 1

    print(rank, end=" ")