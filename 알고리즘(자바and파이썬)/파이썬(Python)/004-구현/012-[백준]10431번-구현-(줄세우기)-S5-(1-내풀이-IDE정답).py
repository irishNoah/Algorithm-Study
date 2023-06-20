# [백준]10431번-구현-(줄세우기)-S5-(1-내풀이-IDE정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10431

'''
# 문제 풀이

* 우선, IDE에서는 정답
* 다른 분의 풀이를 보아하니, 굳이 문제에 주어진 과정에 얽매여야만 하는 것은 아니라서
왜 틀렸는지를 모르겠넴..?
* 좋았던 점
- 예전에는 테스트케이스 번호랑 그 이후의 값들이 한 리스트로 왔을 때
어떻게 구분을 지어야 했었을지 좀 어리버리 했는데 이것을 구분해서 좋았음
- IDE 상에서만 맞고 백준에서는 틀린다고 해서 좀 아쉽기는 하지만
잘 푼 것을 떠나서 주어진 순서대로 사고하고 해결할 수 있었어서 좋았음!

'''
#============================================================

import sys

case = int(sys.stdin.readline())

while True:
    case = case-1

    arr = list(map(int, sys.stdin.readline().split()))
    num = arr[0]; tall = arr[1:]; res = 0

    cmp = []
    if len(cmp) == 0:
        cmp.append(tall[0])

    for i in range(1, len(tall)):
        # cmp의 값보다 새로 할당하려는 키가 더 크면
        # cmp의 맨 뒤에만 추가하고 진행
        if max(cmp) < tall[i]:
            cmp.append(tall[i])

        # 그렇지 않은 경우
        # 총 이동 걸음 구하고, 할당하려는 키의 알맞은 위치에 할당
        else:
            point = len(cmp)
            idx = -1

            for j in range(len(cmp)):
                # 몇 번째에 적합한 키인지 구하기
                idx += 1

                # 총 이동 걸음 수 구하기
                res += point
                point -= 1

                if cmp[j] > tall[i]:
                    break

            # 알맞은 위치에 해당 키 할당
            cmp.insert(idx, tall[i])

    print(num, res, sep=" ")

    if case == 0:
        break