# 2798번 / 블랙잭 / B2
# https://www.acmicpc.net/problem/2798

# 카드의 개수 N과 딜러가 부르는 숫자 M 입력받기
N, M = map(int, input().split())

# 카드의 개수 N에 맞게 값 입력을 리스트로 받기
arrList = list(map(int, input().split()))

sumValue = 0
# 삼중 for문으로 최대값 찾기
for i in range(0, N-2) :
    for j in range(i+1, N-1) :
        for K in range(j+1, N) :
            if arrList[i] + arrList[j] + arrList[K] > M :
                continue
            else :
                sumValue = max(sumValue, arrList[i] + arrList[j] + arrList[K])
                
print(sumValue)