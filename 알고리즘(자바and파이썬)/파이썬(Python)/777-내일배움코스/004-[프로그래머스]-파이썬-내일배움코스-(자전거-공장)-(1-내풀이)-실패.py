# [프로그래머스]-파이썬-내일배움코스-(자전거-공장)-(1-내풀이)-실패.py
# https://github.com/irishNoah/Algorithm-Study
'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건


*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

>>> order의 각 행에 있는 두 번째 요소의 값을 모두 더한다.
- 이게 제작해야 하는 총 대수이다. => bikes
>>> order의 각 행에 있는 첫 번째 요소중 최대값을 찾는다.
- 이게 생산해야 하는 최대 월이다. => maxMonth
>>> make = [0]*month
- 각 월마다 몇 대씩 생산하는지 파악하기 위한 리스트
>>> bikes가 0이 될 때까지 계산
1. bikes를 cost[index][1]로 몫을 구한다. (단, index는 1부터 시작)
    - 만약, 이 몫이 maxMonth보다 작다면
        - make[0:몫]까지 cost[index][1]를 추가 계산
        - 만약, 나머지가 있다면?
            - make[마지막]에 나머지를 추가 계산
        - break
    - 만약, 이 몫이 maxMonth보다 크거나 같다면
        - make[0:마지막]까지 cost[index][1]를 추가 계산
        - bikes = bikes - (cost[index][1] * maxMonth)
>>> 구해진 make를 기반으로 하여 각 make[index]의 cost 값을 계산한다.

??? 만약, 마지막 달까지 계산했는데도 몫이 maxMonth보다 크다면???

'''
#===================================================================================


def solution(cost, order):
    answer = 0
    bikes = sum(i[1] for i in order)
    # print("bikes = ", bikes)

    maxMonth = max(j[0] for j in order)
    # print("maxMonth = ", maxMonth)

    make = [0] * maxMonth
    # print("make = ", make)

    index = 1
    while True:
        print("="*50)
        print("index = ", index)
        print("cost[index][0] = ", cost[index][0])
        print("bikes = ", bikes)
        mok = bikes // cost[index][0]
        print("mok = ", mok)

        if mok < maxMonth:
            # 아래 라인이 내 의도대로 될지는 의문
            # make[0:maxMonth] = make[0:maxMonth] + cost[index][1]

            for i in range(mok):
                make[i] += cost[index][0]

            left = bikes - cost[index][0]*mok
            if left != 0:
                make[-1] += left

            bikes -= (cost[index][0]*mok + left)
            print("makeLast = ", make)

        else:
            # 아래 라인이 내 의도대로 될지는 의문
            # make[0:mok] = make[0:mok] + cost[index][1]

            for i in range(len(make)):
                make[i] += cost[index][0]
            print("makeElse = ", make)
            bikes -= (cost[index][0] * maxMonth)
            print("biesElse = ", bikes)

        if bikes == 0:
            break

        # 인덱스 에러 방지
        if index == len(cost)-1:
            if bikes != 0:
                print("hello")

                mok = bikes // cost[index][0]

                for i in range(mok):
                    make[i] += cost[index][0] * mok

            print("makeIndex = ", make)
            break


        index += 1

    return answer


#===================================================================================

# # 예제 1
# cost = [[0, 10], [50, 20], [100, 30], [200, 40]]
# order = [[3, 50],[7, 200],[8,200]]
# print(solution(cost, order)) # 5000

# 예제 2
cost = [[0, 10], [50, 20]]
order = [[3, 100],[4, 200]]
print(solution(cost, order)) # 4000




# def solution(cost, order):
#     answer = 0
#     return answer