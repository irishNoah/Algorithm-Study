'''
039-[프로그래머스]-PCCP-복습필요(체육대회)-LV2-(1-다른풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/15008/lessons/121684

### 참고
> 다른 사람의 풀이
- https://velog.io/@soorim_yoon/PCCP-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-102-%EC%B2%B4%EC%9C%A1%EB%8C%80%ED%9A%8C

16:40~:16:47
### 설계 분, 총 분
> DFS 활용
- 솔직히 참고했지만 이해 안감

'''

answer = 0
def DFS(L, s, ability, check):
    global answer
    n = len(ability)        # 학생 수
    m = len(ability[0])     # 종목 개수
    
    if L == m:
        answer = max(answer, s)   # 능력치 합의 최댓값을 구함
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                DFS(L+1, s + ability[i][L], ability, check)
                check[i] = 0


def solution(ability):
    global answer
    check = [0]*len(ability)
    DFS(0, 0, ability, check)      
    # Level, sum, ability, check
    # L : level (고를 수 있는 학생 수 중 몇 명째 선택한 것인지), sum : 능력치의 합
    
    return answer