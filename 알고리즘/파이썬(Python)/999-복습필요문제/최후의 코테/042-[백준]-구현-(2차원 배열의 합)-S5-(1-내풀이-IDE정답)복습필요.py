'''
042-[백준]-구현-(2차원 배열의 합)-S5-(1-내풀이-IDE정답)복습필요.py

### 주소
> https://www.acmicpc.net/problem/2167

### 참고
>

13:55 ~ 14:27
### 설계 10분, 총 32분
> 입력받은 i, j, x, y에 대해 각각 -1을 한다.
> for에서 row의 범위 => (i, x-i+1)
    > 각 for 실행시 col의 범위 => (j,y-j+1)
        > hap += arr[row][col]
> hap 출력

'''
#===================================================================================

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []
for _ in range(a):
    arr.append(list(map(int, input().split())))

# print(arr)

k = int(input())

while k != 0:
    k -= 1

    i, j, x, y = map(int, input().split())
    i = i-1; j = j-1; x = x-1; y= y-1
    # print(i, j, x, y)

    hap = 0

    # 주어진 행과 열이 모두 다를 때
    if i != x and j != y:
        for row in range(i, x-i+1):
            for col in range(j, y-j+1):
                # print("arr[row][col] = ", arr[row][col])
                hap += arr[row][col]
        print(hap)

    # 주어진 행과 열이 모두 같을 때
    elif i == x and j == y:
        print(arr[x][y])

    # 주어진 행은 같지만, 열을 다를 때
    elif i == x and j != y:
        for col in range(j, y - j + 1):
            hap += arr[x][col]
        print(hap)

    # 주어진 행은 다르지만, 열을 같을 때
    elif i != x and j == y:
        for row in range(i, x-i+1):
            hap += arr[row][y]
        print(hap)

    # print(hap)

#===================================================================================