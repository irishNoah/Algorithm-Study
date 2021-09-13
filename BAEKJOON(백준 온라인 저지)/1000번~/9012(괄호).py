# 9012 / 괄호 / S4
# https://www.acmicpc.net/problem/9012

# 테스트 케이스 개수 입력
test = int(input())

# 테스트 케이스 개수 만큼 반복
for i in range (test) :
    # 괄호 입력
    value = input()

    # 합계와 관련된 변수 2개를 선언하였는데 그 이유는 다음과 같다.
    # 1) 만약 문제없는 VPS라면 기본적으로 (의 개수와 )의 개수가 같을 것이다.
    # 2) 또한 절대로 (보다 )이 먼저오는 경우는 없어야 한다.
    # 3) 단 )이 먼저오게 된 경우 그 때는 바로 NO 출력을 하고 해당 for문을 탈출한다.
    # 4) 3번에 해당되는 경우가 없을 경우 (와 )의 개수는 동일하며 VPS에 해당된다.

    # 따라서 합계 변수 2개를 가용한 것이다.
    sum = 0
    sum2 = 0

    for j in value :

        if j == '(' :
            sum += 1
            sum2 += 1
        
        elif j == ')' :
            sum -= 1
            sum2 -= 1

        # 만약 (보다 )가 먼저오게 될 경우 NO를 출력하고 for문을 탈출
        if sum2 < 0 :
            print("NO")
            break

    # (와 )의 개수가 동일하며 VPS일 경우 YES 출력
    if sum == 0 :
        print("YES")

    # (와 )의 개수가 동일하지 않을 경우 NO 출력
    elif sum > 0 :
        print("NO")