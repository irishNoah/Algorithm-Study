# [프로그래머스]-파이썬-해시-(추억-점수)-LV1-(1-내풀이-정답)-딕셔너리.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

'''
*** 설계 [총 3분 소요] / 총 풀이 시간[총 10분 소요]
중복된 값도 없으므로 딕셔너리를 활용하면 됨
1. 딕셔너리 infor >>> 키 -> 이름(name[i]) / 값 -> 그리움 점수(yearning[i])
2. photo의 각 배열을 arr로 하고, arr[key]가 딕셔너리에 있으면 sumVal 점수에 더함
3. 이 sumVal 점수를 answer 리스트에 할당
4. 최종적으로 구해진 answer 리스트 출력

'''
def solution(name, yearning, photo):
    answer = []
    
    infor = dict()
    
    # 딕셔너리 생성
    for idx in range(len(name)):
        infor[name[idx]] = yearning[idx]
            
    for arr in photo:
        sumVal = 0 # 각 arr에서 name에 있는 사람들의 그리움 점수만 합산하기 위한 변수
        
        for idx in range(len(arr)):
            if arr[idx] in infor.keys():
                sumVal += infor[arr[idx]]
    
        answer.append(sumVal) # 한 arr에서 구해진 최종 sumVal 할당
    
    return answer