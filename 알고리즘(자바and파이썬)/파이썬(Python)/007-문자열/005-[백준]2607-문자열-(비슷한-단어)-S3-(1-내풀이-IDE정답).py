# [백준]2607-문자열-(비슷한-단어)-S3-(1-내풀이-IDE정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2607

'''
##### 문제 풀이 (시간 제한 > 1초 / 메모리 제한 > 128MB)
* 데이터 최대 개수 100개, 1개 당 최대 길이 10이하 >>> o(n^3) 가능
* 문제 설계 소요 시간 > 18분

* 비슷한 단어의 특징
Case1. 구성 자체가 똑같을 때  (예시 - DOG / GOD)
Case2. 한 단어에서 한 문자를 더했을 때 구성이 똑같은 경우 (예시 - GOD / GOOD)
- keys()로 비교하면 된다. >>> 값이 다를 뿐 키가 같으니까
Case3. 한 단어에서 한 문자를 뺐을 때 구성이 똑같은 경우 (예시 - GOD / GD)
- 첫 번째 단어의 키가 비교하려고 하는 단어의 키에 포함된다!
- in 으로 확인
Case4. 한 단어에서 한 문자를 다른 문자로 변경했을 때 구성이 똑같은 경우 (예시 - GOD / GKD & GOD / GODL)
4-1 입력 단어의 길이가 비교 단어의 길이보다 우선 1이 커야 한다.
4-2 key가 1개만 달라야 한다.
4-3 다른 키의 값이 1이여만 한다!

>>> 단, "DOG"에서 하나의 문자를 더하거나, 빼거나, 바꾸어도 "DOLL"과 같은 구성이 되지는 않으므로
"DOG"과 "DOLL"은 비슷한 단어가 아니다.
- 4-3에 위반됨

* 풀이 설계
1. 단어 개수(N)를 입력 받는다.
2. 첫 번째 단어를 저장할 딕셔너리 cmp 선언
2. for문을 통해 단어를 입력 받는다.
2-1 첫 번째 단어를 입력받고 딕셔너리 cmp에 할당
- 첫 번째 단어 자체는 first에 할당
2-2 이후 단어는 그냥 입력, word에 할당
> 만약 입력 단어가 len(first)보다 길이가 +-2 이상이라면?
- continue
> 그게 아니라면?
- 입력 받고 dict()에 할당 >>> 3으로 간다.
3. 입력 받은 dict와 cmp와 비교 - 비교 변수 : cnt
> case1~4에 해당되면 cnt값 1 증가 & 해당 for문 종료
4. for문 종료 후 - cnt 출력

* 헣헣 왜 IDE예서만 정답이었을까?

'''
#============================================================

import sys

N = int(sys.stdin.readline().rstrip())
flag = False # 첫 번째 단어가 있는지 없는지 판별
cmp = {}
cnt = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    # 첫 번째 입력받은 단어 dict()인 cmp 할당
    if flag == False:
        flag = True
        first = word

        for chr in word:
            if chr in cmp:
                cmp[chr] += 1
            else:
                cmp[chr] = 1

        continue

    if len(word) <= len(first)-2 or len(word) >= len(first)+2:
        continue

    dic = {}
    for chr in word:
        if chr in dic:
            dic[chr] += 1
        else:
            dic[chr] = 1

    # case 1
    if cmp == dic:
        cnt += 1
        continue

    # case 2
    elif cmp.keys() == dic.keys():
        cnt += 1
        continue

    # case 4
    '''
    4-1 입력 단어의 길이가 비교 단어의 길이보다 우선 1이 커야 한다. >>> 이건 입력 때 파악
    4-2 입력된 단어의 key가 1개가 더 많아야 한다. >>> 즉, cmp에 없는 key
    4-3 다른 키의 값이 1이여만 한다!
    '''
    if len(dic.keys()) >= len(cmp.keys()):
        find = 0

        for key in dic.keys():
            if key not in cmp.keys():
                find = dic[key]
                break

        if find == 1:
            cnt += 1

        continue

    # case 3
    case3 = 0

    for key in dic.keys():
        if key not in cmp.keys():
            case3 += 1
            idx = key

    if case3 == 1 and dic[idx] == 1:
        cnt += 1
        continue

    else:
        continue

print(cnt)