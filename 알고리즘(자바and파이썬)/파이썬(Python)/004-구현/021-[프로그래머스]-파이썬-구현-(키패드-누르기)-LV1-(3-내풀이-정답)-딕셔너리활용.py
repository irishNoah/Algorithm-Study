# [프로그래머스]-파이썬-구현-(키패드-누르기)-LV1-(3-내풀이-정답)-딕셔너리활용.py
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

* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 키패드를 딕셔너리 활용해 키-값 매핑한다. (키 : 번호 / 값 : 좌표)
- left = [1,4,7] / right = [3, 6, 9]
- for문을 활용해 답을 구한다.

'''
#===================================================================================

def solution(numbers, hand):
    answer = ''

    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left = [1, 4, 7]; right = [3, 6, 9]
    handL = '*'; handR = '#'


    for val in numbers:

        if val in left:
            answer += 'L'
            handL = val

        elif val in right:
            answer += 'R'
            handR = val

        else:
            curNow = pad[val]
            curL = pad[handL]
            curR = pad[handR]

            minL = abs(curNow[0]-curL[0]) + abs(curNow[1]-curL[1])
            minR = abs(curNow[0] - curR[0]) + abs(curNow[1] - curR[1])

            if minL < minR:
                answer += 'L'
                handL = val

            elif minL > minR:
                answer += 'R'
                handR = val

            else:
                if hand == "left":
                    answer += 'L'
                    handL = val
                else:
                    answer += 'R'
                    handR = val

    return answer

# #############################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))