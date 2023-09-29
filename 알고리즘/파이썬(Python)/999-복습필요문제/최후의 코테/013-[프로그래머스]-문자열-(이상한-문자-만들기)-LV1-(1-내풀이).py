'''
013-[프로그래머스]-문자열-(이상한-문자-만들기)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/12930

### 설계 5분, 총 20분
1. 메소드 정확히 기억하기
> 소문자 to 대문자
- toUpper() : X / upper(): ㅇ
> 대문자 to 소문자
- toLower() : X / lower(): ㅇ

2. 설계의 중요성
>>> 입출력 예시에서는 공백이 단어 사이에 하나만 있지만, 
사실 공백이 여러개 연달아 이어서 있을 수 있다.
>>> 또한, 단어 사이에만 공백이 있는 게 아니라 맨 처음과 맨 끝에도 있을 수도 있다.
>>> 따라서, 공백 여부에 대한 Flag 변수를 활용해서 해결했다.

'''

def solution(s):
    
    ans = ""    # 리턴 문자열
    flag = True # 공백 여부, True일 경우 공백이라 간주
    idx = 0     # 각 단어의 인덱스
    
    
    for val in s:
        ### 공백 여부 확인
        if val == ' ':
            flag = True
            idx = 0   # 공백일 경우, 각 단어의 인덱스를 0으로 초기회
            ans += val
        
        else:
            flag = False
        
        # 공백 여부 기준으로 단어 변형 Go
        if flag == False:
            if idx % 2 == 0:
                ans += val.upper()
            else:
                ans += val.lower()
            
            idx += 1
    
    return ans