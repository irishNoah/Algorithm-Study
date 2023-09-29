# [프로그래머스]-파이썬-구현-(키패드-누르기)-LV1-(3-내풀이-정답)-딕셔너리 활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

'''
*** 참고 URL

*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)


*** 설계 [10분 소요] / 총 풀이 시간[총 28분 소요]
- dict()를 활용해서 0~9 숫자(키)의 각 좌표를 x,y(값)의 개념으로 세팅한다. => pos
- 처음에는 왼손은 *, 오른손은 #의 위치에 있다고 가정한다. > lHand = *, 오른손 = #
- 1,4,7은 왼손이 누르게 하고, 해당 숫자를 누를 경우 왼손의 위치를 해당 숫자에 세팅한다. > lHand = 숫자
- 3,6,9은 오른손이 누르게 하고, 해당 숫자를 누를 경우 오른손의 위치를 해당 숫자에 세팅한다. > rHand = 숫자
- 2,5,8,0이 누를 경우 이 숫자의 좌표와 왼손의 위치값(lPos) 및 오른손의 위치값(rPos)을 빼서 절댓값이 작은 것을
할당하고, 그 손에 해당 위치를 놓는다.
    - 단, 절댓값이 동일한 경우, 주손을 할당한다.

*** 정확성 테스트



'''
# #############################################################

def solution(numbers, hand):

    pos = {  # 키패드 각 숫자 또는 문자의 위치값
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2),
    }

    lHand = '*'; rHand = '#'
    answer = ""

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            lHand = num

        elif num in [3, 6, 9]:
            answer += "R"
            rHand = num

        else:
            lPos = pos[lHand]; rPos = pos[rHand]; curPos = pos[num]

            leftToCur = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rightToCur = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if leftToCur < rightToCur:
                answer += "L"
                lHand = num
            elif leftToCur > rightToCur:
                answer += "R"
                rHand = num
            else:
                if hand == "left":
                    answer += "L"
                    lHand = num
                else:
                    answer += "R"
                    rHand = num

    return answer


# #############################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand)) # result = "LRLLLRLLRRL"