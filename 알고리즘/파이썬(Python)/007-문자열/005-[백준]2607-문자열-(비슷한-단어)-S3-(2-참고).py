# [백준]2607-문자열-(비슷한-단어)-S3-(2-참고).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2607

'''
* 참고 URL 
>>> https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-2607-%EB%B9%84%EC%8A%B7%ED%95%9C-%EB%8B%A8%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

문자열 비교 문제. 입력 값의 수가 널널하므로 모든 문자를 다 체크해주면 된다.
새로운 단어(word)가 입력될 때마다 비교 대상 문자(첫 단어, target)가 담긴 리스트를 복사한다. 복사된 리스트는 compare이라고 이름 붙였다.

새로운 단어 문자열을 for문을 돌리면서 compare에 해당 문자가 포함되어 있는지 확인한다.
있으면 remove하고, 없으면 cnt 값을 하나 늘린다.

순회가 완료된 뒤의 cnt 값은 target 단어에 포함되지 않은 word의 문자의 개수이고, compare에 남아있는 문자들은 word에 포함되지 않은 문자들이다.

따라서 cnt 값과 compare의 길이가 각각 1 이하여야만 조건을 만족하는 '비슷한 단어'이다.

'''
#============================================================

N = int(input())
target = list(input()) # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(N-1):
    compare = target[:]
    word = input() # 새로운 단어
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)