# [백준]2870-문자열-(수학숙제)-S4-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2870

'''
# 문제 풀이

# 핵심
- 글자 N줄
- 각 글들은 숫자 및 소문자로만 이루어져있음
- 각 글들의 길이는 최대 100글자이다.

# 조건
- 각 글들의 숫자를 모두 찾고, 이 숫자를 비내림차순(=오름차순)으로 정리해야 한다.
- 숫자 앞에 '0'이 있는 경우는 정리하면서 생략 가능하다.

# 문제 설계
- 글자 개수 N을 입력 받는다
- for문을 통해 N개에 맞는 단어들을 입력 받는다
> 각 글자의 첫번째가 숫자라면 value 변수에 더한다. 
> 이후에는 ord()를 활용해서 ord('0') ~ ord('9') 사이에 있는 것이라면 value라는 변수에 더한다.
> 없다면 value를 리스트 변수에 할당하고 초기화한다. (단, 할당할 때는 int 타입으로 변환하고 할당한다.)
- for문이 다 끝나면 리스트 정렬을 해준다.
- 차례대로 int형으로 변환해 출력한다.

'''
#============================================================

N = int(input())

arr = []

for _ in range(N):
    word = input() # 단어 입력
    value = ""

    if ord('0') <= ord(word[0]) <= ord('9'):
        value += word[0]

    for i in range(1, len(word)):
        if ord('0') <= ord(word[i]) <= ord('9'):
            value += word[i]

            # 마지막 인덱스가 숫자일 경우는 바로 할당
            if i == len(word)-1:
                arr.append(int(value))


        else:
            if value != "":
                arr.append(int(value))
                value = ""

arr.sort()

for j in range(len(arr)):
    print(int(arr[j]))




