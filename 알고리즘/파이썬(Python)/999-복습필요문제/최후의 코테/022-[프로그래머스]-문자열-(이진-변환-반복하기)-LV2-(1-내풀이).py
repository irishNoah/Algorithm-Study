'''
022-[프로그래머스]-문자열-(이진-변환-반복하기)-LV2-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/60057

### 설계 7분, 총 17분
* 스택 사용
0. while문 이전에 s를 리스트화한다.
1. while문에서 len(s) != 1 일 때까지 반복 수행한다. >>> 큰 while문(진짜 s가 1이 될 때까지)
    2. while문에서 len(s) != 0일 때까지 반복 수행한다. >>> 작은 while문(주어진 s에서 0과 1의 갯수 파악용)
        주어진 s에서 차례대로 pop() 메소드로 s의 요소를 꺼낸다.
        > 이 요소가 '0'일 경우 cntZero += 1 (cntZero는 0의 개수를 세는 변수)
        > 이 요소가 1일 경우 cntOne += 1 (cntOne은 1의 개수를 세는 변수)
    3. cntOne을 기준으로 이진수화 한 이후, 리스트화하여 s에 대입한다.
        > 그러고 나서 cntOne = 0으로 초기화한다.
    4. repeat += 1 (repeat은 이진 변화 개수)
5. return [repeat, cntZero]

'''

def solution(s):
    s = list(s)
    cntZero = 0; cntOne = 0; repeat = 0
    
    while len(s) != 1:
        while len(s) != 0:
            cmp = s.pop()

            if cmp == '0':
                cntZero += 1
            else:
                cntOne += 1
        
        s = str(bin(cntOne)) # 이렇게 하면 '0b111'과 같은 형태로 앞에 0b가 붙는다.
        s = s[2:] # 그래서 앞에 0b를 슬라이싱을 통해 제거해주자
        s = list(s) # 이진 변화 결과 대입
        cntOne = 0
        
        repeat += 1 # 이진 변환 횟수
    
    return [repeat, cntZero]