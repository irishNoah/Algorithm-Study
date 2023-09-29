'''
025-[프로그래머스]-구현-(키패드-누르기)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/67256

### 설계 11분, 총 25분
1. 키패드에서 숫자를 키로, 숫자의 위치를 담은 (x,y)를 값으로 하는 딕셔너리 생성
2. 왼손의 '*' 위치를 posL, 오른손의 '#' 위치를 posR로 한다.
3. numbers를 돈다.
    > 숫자가 1,4,7일 경우에
        > answer에 "L"을 더하고 posL에 해당 숫자의 위치를 할당한다.
    > 숫자가 3,6,9일 경우에
        > answer에 "R"을 더하고 posR에 해당 숫자의 위치를 할당한다.
    > 숫자가 2,5,8,0일 때
        > 해당 숫자의 위치와 posL과 posR의 위치의 절댓값을 구한다.
            > 만약, 두 손의 절댓값이 다를 경우
                > 절댓값이 낮은 손을 answer에 더한다.
                > 절댓값이 낮은 posL 또는 posR에 해당 위치를 할당한다.
            > 만약, 두 손의 절댓값이 같을 경우
                > answer에 주손(L 또는 R)을 할당한다.
                > 해당 주손인 posL 또는 posR에 해당 위치를 할당한다.

'''

def solution(numbers, hand):
    answer = ""
    
    phone = {
        1 : [0,0], 2 : [0,1], 3 : [0,2],
        4 : [1,0], 5 : [1,1], 6 : [1,2],
        7 : [2,0], 8 : [2,1], 9 : [2,2],
        '*' : [3,0], 0 : [3,1], '#' : [3,2]
    }
    
    posL = phone['*']; posR = phone['#']
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            posL = phone[num]
        
        elif num in [3,6,9]:
            answer += "R"
            posR = phone[num]
    
        else:
            distL = abs(phone[num][0]-posL[0]) + abs(phone[num][1]-posL[1])
            distR = abs(phone[num][0]-posR[0]) + abs(phone[num][1]-posR[1])
    
            if distL < distR:
                answer += "L"
                posL = phone[num]
            elif distL > distR:
                answer += "R"
                posR = phone[num]
            else:
                if hand == "left":
                    answer += "L"
                    posL = phone[num]
                else:
                    answer += "R"
                    posR = phone[num]
    return answer