# [백준]15650-(N과M(2))-(백트레킹)-S3-(2-참고-)-그래프+백트래킹.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/15650

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 11분 소요] / 총 풀이 시간[총 -분 소요]
- 코드 참고

*** 참고

'''
#===================================================================================

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = []

# [2,1]과 같이 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외하기 위해
# start부터 N까지의 숫자를 사용
def back(start):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(start, N + 1):
        if i not in ans:
            ans.append(i)
            # 재귀함수를 호출할 때는 i를 이용해 자신의 다음 숫자를 부름
            back(i + 1)
            ans.pop()


back(1)
#===================================================================================