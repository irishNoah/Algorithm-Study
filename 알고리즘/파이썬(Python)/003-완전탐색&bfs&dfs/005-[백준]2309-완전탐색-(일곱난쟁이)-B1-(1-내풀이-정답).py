# [백준]2309-완전탐색-(일곱난쟁이)-B1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2309

'''
* 제한 > 시간 : 2초 / 메모리 : 128MB
- 시간 제한이 2초이기 때문에 탐색 문제일 가능성이 높다.
- 난쟁이의 수 > 9명
- 각 난쟁이의 키 > 100 미만
- 이것을 통해 완전탐색의 스멜을 맡을 수 있다.

* 설계
> 입력 받은 이후 itertools의 조합을 활용하여 9명 중 7명을 뽑아 sum을 시킨 후
100이 되는 조합을 찾는다
- itertools의 combinations 활용하기
> 어차피, 가능한 정답이 여러개일 경우 아무거나 출력한다고 했으니
찾자마자 출력하고 프로그램을 종료한다.

'''
#============================================================

import sys
import itertools

arr = []
for _ in range(9):
    tall = int(sys.stdin.readline().rstrip())
    arr.append(tall)


combi = list(itertools.combinations(arr, 7)) # 조합
for i in range(len(combi)):
    if sum(combi[i]) == 100:
        res = sorted(combi[i])

        for j in range(len(res)):
            print(res[j])

        break