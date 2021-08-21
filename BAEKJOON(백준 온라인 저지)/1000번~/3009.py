# 3009번 / 네 번째 점 / B3
# https://www.acmicpc.net/problem/3009

cnt = 0
arrX = []
arrY = []

while True :
    x, y = map(int, input().split())
    x = int(x)
    y = int(y)

    arrX.append(x)
    arrY.append(y)

    cnt += 1

    if cnt == 3 :
        break

# 오름차순 정렬
arrX.sort()
arrY.sort()

xPoint = 0
yPoint = 0

# 오름차순 정렬된 것 중에서 배열 요소 0번째와 1번째 값이 같은 경우
# 2번째 값만 혼자 있는 것이므로 2번째 값이 나머지 하나의 값이 되고,
# 0번째와 1번째 값이 다른 경우 1번째와 2번째 값이 같고 0번째 값만 다르므로
# 0번째 값이 나머지 하나의 값이 된다.
if arrX[0] == arrX[1] :
    xPoint = arrX[2]
elif arrX[0] != arrX[1] :
    xPoint = arrX[0]

if arrY[0] == arrY[1] :
    yPoint = arrY[2]
elif arrY[0] != arrY[1] :
    yPoint = arrY[0]

print(xPoint, yPoint)