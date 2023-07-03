# [프로그래머스]-파이썬-구현-(키패드-누르기)-LV1-(1-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/67256?language=python3

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)
> numbers 배열의 크기는 1 이상 1,000 이하입니다.
> numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
> hand는 "left" 또는 "right" 입니다.
> "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
> 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

*** 조건
1> 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2> 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3> 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4> 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    > 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
5> 연속된 문자열 형태로 return 하도록 solution 함수를 완성

* 설계 [총 15분 소요] / 총 풀이 시간[총 50분 소요]
> 전화번호 키패드 : 2차원 리스트 pad 에 생성
> 결과값 문자열 answer 할당
> numbers : 1차원 입력 리스트 / hand : 주손
> 1,4,7 : posLI, posLJ에 I, J 할당
> 3,6,9 : posRI, posRJ에 I, J 할당
> 2, 5, 8, 0
- 해당 I,J 값을 posLI, posLJ와 posRI, posRJ와 차를 구한 이후
절대값이 더 적은 것을 answer에 추가 (단, 절대값 같을 경우 주손을 할당)
- 정해진 손에 맞게 posLI, posLJ 또는 posRI, posRJ 할당

*** 2차원 리스트에서 인덱스 가로 세로 값 찾기
> https://minjoos.tistory.com/2

*** 50분이나 걸린 이유
> numbers[i]의 값이 2차원 리스트 pad 중에 있는 값과 일치하는 것의 위치가 어디인지 찾을 때
- 예 > findL = [(i,j) for i in range(4) for j in range(3) if pad[i][j]==numbers[i]]

이렇게 찾았었다. 이것 때문에 틀린 것이다. numbers[i]와 findL 안에 있는 for문의 i가 겹쳤기 때문이다...

findL = [(j,k) for j in range(4) for k in range(3) if pad[j][k]==numbers[i]]

이렇게 하니까 맞았다. 앞으로는 겹치는 인덱스가 발생한다면, 무조건 다 다른 인덱스로 사용하도록 하자.....

'''
#============================================================

import sys

def solution(numbers, hand):
    answer = ''

    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    posLI= 3; posLJ = 0; posRI = 3; posRJ = 2;


    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'

            findL = [(j,k) for j in range(4) for k in range(3) if pad[j][k]==numbers[i]]
            posLI = findL[0][0]; posLJ = findL[0][1];

        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'

            findR = [(j,k) for j in range(4) for k in range(3) if pad[j][k]==numbers[i]]
            posRI = findR[0][0]; posRJ = findR[0][1];

        elif numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0: #0
            findX = [(j,k) for j in range(4) for k in range(3) if pad[j][k]==numbers[i]]
            posXI = findX[0][0]; posXJ = findX[0][1];

            # 절대값 구하기
            minL = abs(posXI-posLI) + abs(posXJ-posLJ)
            minR = abs(posXI-posRI) + abs(posXJ - posRJ)

            # 최소값 구하기
            if minL == minR:
                if hand == 'left':
                    answer += 'L'
                    posLI = posXI
                    posLJ = posXJ

                else:
                    answer += 'R'
                    posRI = posXI
                    posRJ = posXJ

            else:
                if minL < minR:
                    answer += 'L'
                    posLI = posXI
                    posLJ = posXJ

                else:
                    answer += 'R'
                    posRI = posXI
                    posRJ = posXJ

    return answer

# #############################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))

# pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
# newlist=[(i,j) for i in range(4) for j in range(3) if pad[i][j]==0]
# print(type(newlist[0][0]), type(newlist[0][1]));
