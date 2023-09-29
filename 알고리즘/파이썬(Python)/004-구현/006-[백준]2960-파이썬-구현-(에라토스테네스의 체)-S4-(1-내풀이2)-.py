# [백준]2960-파이썬-구현-(에라토스테네스의 체)-S4-(1-내풀이2)-.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2960

'''
# 느낀점

IDE 상에서는 주어진 테스트케이스가 다 맞았다.
틀린 사유도 메모리 초과나 시간 초과가 아니라 "실패"로 떴다.
어떤 것이 원인인 지는 모르겠다.
'''

def solution(n, k):

    arr = [i for i in range(2, n+1)]
    answer = -1

    res = []

    while 1:
        idx = arr.index(min(arr))
        check = min(arr)

        for i in range(idx, len(arr)):
            if arr[i] == 999:
                continue

            else:

                if arr[i] % check == 0:
                    res.append(arr[i])

                    if len(res) == k:
                        answer = res[-1]
                        break

                    arr[i] = 999

                if i == len(arr)-1:
                    break

        if answer != -1:
            break

    return answer

n, k = map(int, input().split())
print(solution(n, k))