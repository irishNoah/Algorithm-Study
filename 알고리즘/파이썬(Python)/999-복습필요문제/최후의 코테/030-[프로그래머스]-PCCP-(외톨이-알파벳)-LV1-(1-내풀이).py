'''
030-[프로그래머스]-PCCP-(외톨이-알파벳)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/15008/lessons/121683

### 참고
> 없음

### 설계 3분, 총 12분
* 딕셔너리를 활용한다.
1. for문 활용해서 딕셔너리 구하기
> 만약, 처음 들어오는 알파벳이면?
    - 딕셔너리에 알파벳을 키로, 값을 1로 세팅
> 만약, 처음 들어오는 알파벳이 아니라면?
    - 문자열에서 앞의 알파벳이 현재 알파벳과 동일한지 비교
        - 다를 경우에만 해당 알파벳의 숫자 값 1 증가
2. for문을 돈다.
    - k, v 기준
        - v가 1인 경우에는 외톨이 알파벳 아니다.
        - v가 1보다 큰 경우에는 외톨이 알파벳이다.
            - 이런 경우, k를 answer 리스트에 할당한다.
3. 최종적으로 구해진 answer
    - 만약, answer의 길이가 0인 경우에는 "N"을 리턴한다.
    - 그렇지 않은 경우, answer을 오름차순 정렬 후, join한 상태로 리턴한다.

'''

def solution(input_string):
    answer = []
    input_string = list(input_string)
    
    cnt = dict()
    for idx in range(len(input_string)):
        if cnt.get(input_string[idx]) == None:
            cnt[input_string[idx]] = 1
            continue
        
        if input_string[idx] != input_string[idx-1]:
            cnt[input_string[idx]] += 1
            
    for k, v in cnt.items():
        if v > 1:
            answer.append(k)
    
    if len(answer) == 0:
        return "N"
    
    
    answer.sort()
    return "".join(answer)