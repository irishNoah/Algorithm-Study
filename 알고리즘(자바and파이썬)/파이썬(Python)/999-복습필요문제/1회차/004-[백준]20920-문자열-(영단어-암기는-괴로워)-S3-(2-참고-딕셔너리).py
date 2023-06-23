# [백준]20920-문자열-(영단어-암기는-괴로워)-S3-(2-참고-딕셔너리).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/20920

'''
##### 문제 풀이

# 내 풀이와 다른 점
- 설계는 나와 동일하다
- 다만, 나는 리스트, 이 사람은 딕셔너리를 활용했을 뿐
- 데이터의 개수가 10만개인 것을 감안했을 때 O(N logN)인 것을 활용했어야 했는데,
내가 푼 코드는 최대 2차원이다 보니 시간초과 판정 나는 것은 당연하다.

'''
#============================================================

import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # 단어 개수, 단어 길이
word_lst = {}  # 딕셔너리

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:  # 단어가 M미만인 경우
        continue
    else:  # 단어가 M이상인 경우
        if word in word_lst:  # 단어가 있는 경우
            word_lst[word] += 1
        else:  # 단어가 없는 경우
            word_lst[word] = 1

word_lst = sorted(word_lst.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))  # x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in word_lst:
    print(i[0])



