'''
015-[프로그래머스]-해시-(평행)-LV0-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/120875

### 설계 5분, 총 10분

'''

def solution(dots):
    answer = 0
    flag = False # 평행 여부 
    

    # A-B / C-D 세트
    if (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]):
        flag = True
    
    # A-C / B-D 세트
    elif (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0]):
        flag = True
    
    # A-D / B-C 세트
    elif (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0]) == (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0]):
        flag = True
    
    if flag == True:
        return 1
    else:
        return 0