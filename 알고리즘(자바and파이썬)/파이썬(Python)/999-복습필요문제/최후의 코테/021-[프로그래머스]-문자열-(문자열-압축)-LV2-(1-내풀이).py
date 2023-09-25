'''
021-[프로그래머스]-문자열-(문자열-압축)-LV2-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/60057

### 설계 5분, 총 42분
> 참고
- https://ljhyunstory.tistory.com/18

'''

def solution(s):
    result=[]
    
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):            # i자씩 끊기!
        b = ''
        cnt = 1                             # 갯수 체크
        tmp=s[:i]                           # 첫번째 미리 자르기

        for j in range(i, len(s)+i, i):     # i부터 끝까지 i단위로 나누어 탐색
            
            if tmp==s[j:i+j]:               # 앞과 같으면 
                cnt+=1                      # 카운트
            else:                           # 아니면
                if cnt!=1:                  # 앞에서 중복이 있었다!
                    b = b + str(cnt)+tmp    # 글자 만들기(b라는 새로운 압축 문자열을 만들어주기)
                else:
                    b = b + tmp
                    
                tmp=s[j:j+i]
                cnt = 1
                
        result.append(len(b))
        

    return min(result)