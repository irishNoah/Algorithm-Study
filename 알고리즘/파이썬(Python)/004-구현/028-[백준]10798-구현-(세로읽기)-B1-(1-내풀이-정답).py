# [백준]10798-구현-(세로읽기)-B1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10798

'''
*** 참고 URL

*** 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)

*** 조건

*** 설계 [3분 소요] / 총 풀이 시간[총 분 소요]
- 애초에 '*'로 채워진 리스트 생성
    - 리스트명 : arr / 행 : 5개, 한 행당 총 15개의 * 존재
- for문을 통해 입력
    - 입력 받은 각 word의 len을 구해서 최고 길이를 구한다. (변수명 leng)
- for문을 통해 세로로 읽게 한다. (범위 range(0, leng))
    - 만약, arr[i][j]가 '*'일 경우 패스한다.


'''
#============================================================

import sys

arr = [['*']*15 for _ in range(5)]
# print(arr)

leng = 0

maxLeng = 0

for i in range(5):
    word = sys.stdin.readline().rstrip()

    if maxLeng < len(word):
        maxLeng = len(word)

    arr[i][:len(word)] = list(word)

# print(arr)

answer = ""
for j in range(maxLeng): # 열
    for i in range(5): # 행
        if arr[i][j] == '*':
            continue

        answer += arr[i][j]

print(answer)