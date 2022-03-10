# 프로그래머스 LV1 - 부족한 금액 계산하기
# 분류 - 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/82612

# 정확성 테스트의 케이스 23개 중 23개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(price, money, count):
    answer = 0 # 리턴할 값 answer

    # 타는 횟수에 따른 금액을 할당하기 위한 변수 sum_money
    sum_money = 0

    # for문을 통해 sum_money 계산하기
    for i in range(1, count+1):
        sum_money += price * i

    # sum_money가 money보다 크거나 같으면 필요한 이용 금액 산출하기
    if sum_money >= money :
        answer = sum_money - money

    return answer

price = 3
money = 20
count = 4
print(solution(price, money, count)) # 출력 예 : 10