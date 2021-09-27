# 2004 / 조합 0의 개수 / S2
# https://www.acmicpc.net/problem/2004

# 공백으로 구분하여 두 개의 정수 값 입력
a, b = map(int, input().split())

# 구하고자 하는 팩토리알에서 소인수 중 2의 개수를 파악하는 함수 count_two() 함수 선언
def count_Two(n) :
    cntTwo = 0
    while n != 0 :
        n = n // 2
        cntTwo += n

    return cntTwo

# 구하고자 하는 팩토리알에서 소인수 중 5의 개수를 파악하는 함수 count_Five() 함수 선언
def count_Five(n) :
    cntFive = 0
    while n != 0 :
        n = n // 5
        cntFive += n

    return cntFive

# 기본적으로 조합은 nPv 라고 했을 때 "n! / r! * (n-r)!"이다.
# 즉, n!에 있는 2와 5의 개수, r!에 있는 2와 5의 개수, (n-r)!에 있는 2와 5의 개수를 각각 구한 후
# 2의 개수를 구한 것과 5의 개수를 구한 것을 출력해주면 된다.
getTwo = count_Two(a) - count_Two(b) - count_Two(a-b)
getFive = count_Five(a) - count_Five(b) - count_Five(a-b)

print(min(getTwo, getFive))