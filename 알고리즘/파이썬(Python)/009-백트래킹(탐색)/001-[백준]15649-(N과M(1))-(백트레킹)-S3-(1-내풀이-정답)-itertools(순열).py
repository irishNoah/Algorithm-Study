# [백준]15649-(N과M(1))-(백트레킹)-S3-(1-내풀이-정답)-itertools(순열).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/15649

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 22분 소요]
1. 1부터 N까지 for문을 활용해서 리스트 arr에 담아낸다.
2. 조합을 활용해서 permutations(arr, M) 을 통해 결과를 출력한다.

*** 참고
> https://531522szerodesire.tistory.com/87


'''
#===================================================================================

import itertools

N , M = map(int, input().split())

arr = [i for i in range(1, N+1)]

for val in itertools.permutations(arr, M):
    # 단순하게 val[0:M]은 튜플 타입이기 때문에
    # list()화 해준 이후 *(아스터리크)를 붙여 출력한다.
    print(*(list(val[0:M])))



#===================================================================================

