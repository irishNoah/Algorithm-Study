# [백준]1213-구현-(팰린드롬-만들기)-S3-(1-내풀이-IDE정답&시간초과).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1213

'''
*** 참고 URL
https://star7sss.tistory.com/391

*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건


*** 설계 [총 13분 소요] / 총 풀이 시간[총 50분 소요]
> 입력받은 문자열을 dict화
> 입력받은 키의 값 중에서 홀수인 것은 하나만 있어야 한다!
    > 이게 거짓이면
        > I'm Sorry Hansoo 출력
    > 이게 참이면
        > keys()를 활용해 key값을 모은 리스트(list_key) 생성 && sort
            > list_key를 permutations를 활용해 경우의 수 구하기
                > 첫 번째로 구해진 팰린드롬이 답

*** 틀린 이유
- 시간 초과

'''
#============================================================

import sys
from itertools import permutations

word = sys.stdin.readline().rstrip()


list_word = list(word)

dict_word = dict()
for cnt in list_word: # 리스트에 있는 거 dict에 추가하기
    if dict_word.get(cnt) == None:
        dict_word[cnt] = 1
    else:
        dict_word[cnt] += 1

cnt_odd = 0
for check in dict_word.values():
    if check % 2 == 1:
        cnt_odd += 1

if cnt_odd > 1:
    print("I'm Sorry Hansoo")
    sys.exit(0)

else:
    answer = ""
    list_word = sorted(list_word)
    # flag = True ### flag 위치가 여기면 안된다.

    for cmp in permutations(list_word, len(list_word)):
        test = "".join(map(str, cmp))
        flag = True # 헣허 flag 위치 때문에... 시간 잡아 먹었노

        for i in range(0, len(test) // 2):
            if test[i] != test[(len(test) - 1) - i]:
                flag = False
                break

        if flag == False:
            continue
        else:
            answer = test
            break

    print(answer)
