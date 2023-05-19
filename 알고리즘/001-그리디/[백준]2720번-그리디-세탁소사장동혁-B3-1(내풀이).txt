# [백준]2720번-그리디-세탁소사장동혁-B3-1(내풀이)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2720

coin = [25, 10, 5, 1] # 잔돈 종류

testCase = int(input()) # 테스트케이스 개수 입력

caseCount = 0 # while문을 돈 횟수

while True:
    caseCount += 1

    money = int(input()) # 지불할 값 입력

    cnt = [0] * 4 # 각 잔돈의 종류의 개수를 저장하기 위한 리스트

    # 각 잔돈 종류에 대한 개수 구하기
    for i in range(0, 4):
        if (money // coin[i]) > 0:
            mok = money // coin[i] # 각 잔돈의 종류로 나눈 몫 구하기
            
            cnt[i] = mok

            money = money - (coin[i] * mok)

        # left가 0이 된다면, 더이상 for를 돌 필요가 없음
        if money == 0:
            break
    
    
    print(*cnt) # 한 줄에 출력 --- 애초에 이렇게 하면 알아서 각 값을 공백을 두어 출력

    # while문 탈출 조건
    if caseCount == testCase:
        break