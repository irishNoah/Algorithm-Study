# [백준]2960-파이썬-구현-(에라토스테네스의 체)-S4-(1-내풀이)-실패.py
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

    while 1:
        # 이미 제거된 거 제외하고 남은 값 중에서 최소값 할당
        check = min(arr)

        for i in range(len(arr)):
           if arr[i] == 999:
               continue

           if arr[i] != 999 and arr[i] % check == 0:
                k -= 1

                if k == 0:
                    answer = arr[i]
                    break

                # arr[i]가 999면 제거됐다는 의미
                arr[i] = 999

        if answer > -1:
            break

    return answer

n, k = map(int, input().split())
print(solution(n, k))