# [백준]2563번-구현-(색종이)-S5-(2-다른풀이)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2563

N = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)

'''
1. 난 매우 수학적으로 접근하여 풀었다.
2. 하지만, 수학적으로 접근할 경우 겹치는 횟수가 몇 개냐에 따라서 수식이 매우 복잡해질 수 있다.
- 만약, 동일한 부분에 대해서 100번 겹칠 경우, 이걸 일일이 계산???
3. 하지만, 주어진 수 x와 y이에서 +10(정사각형이니까)까지 for문으로 해당하는 범위 내를 1과 같은 수나 문자로 채운 이후
최종적으로 채운 수 또는 문자를 count()해서 구한다면?
'''