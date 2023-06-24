# [백준]20920-문자열-(영단어-암기는-괴로워)-S3-(3-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/20920

'''
* 제한 > 시간 : 1초 / 메모리 : 1024MB

* 조건
0. 길이가 M이상인 단어들만 외운다
1. 자주 나오는 단어일수록 앞에 배치한다.
2. 해당 단어의 길이가 길수록 앞에 배치한다.
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

* 설계
1. 단어 개수(N) & 길이(M) 입력
2. 단어 입력
> 길이가 M 미만이면 continue
> 사전에 있나 확인(키로 찾는다)
- 있다면 value를 1 증가
- 없으면 value를 1로 하고 사전에 추가
3. 사전에 다 추가한 이후
- 정렬 : 값 빈도 >> len(단어[키]) >> 단어
4. 출력(한 줄에 한 단어)

'''
#============================================================

import sys

N, M = map(int, sys.stdin.readline().split())

dic = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    # print(word)

    if len(word) < M:
        continue

    if dic.get(word) == None:
        dic[word] = 1
    else:
        dic[word] += 1

res = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for sec in res:
    print(sec[0])