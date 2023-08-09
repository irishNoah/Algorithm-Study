# [백준]15649-(N과M(1))-(백트레킹)-S3-(2-참고)-그래프+백트래킹.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/15649

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 코드 참고

*** 참고
> https://veggie-garden.tistory.com/24

'''
#===================================================================================

N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:  ### 배열의 길이를 확인
        print(" ".join(map(str, ans)))  ### 1 2 3 이런 상태로 출력하기 위해
        # print("ans = ", ans)
        # print("hello")

        return
    for i in range(1, N + 1):  ### 1 ~ N 까지
        # print("i = ", i)
        if i not in ans:  ### 중복 확인
            # print("append")
            ans.append(i)  ### 배열 추가
            back()  ### 재귀
            ### return으로 돌아오면 이게 실행됨. 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것
            ans.pop()

back()

#===================================================================================