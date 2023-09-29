# [프로그래머스]-파이썬-동적계획법-(행운의-오색사탕)-(1-내풀이-실패).py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

*** 참고

'''
#===================================================================================

def solution(candy, positions):
    answer = []

    case = len(positions)

    while True:
        case -= 1

        for i in range(len(positions)):
            print("=" * 50)
            if positions[i] == 1:
                answer.append(0)
                continue

            cnt = 0
            K = positions[i]
            print("set K = ", K)
            arr = candy[:K]
            print("set arr = ", arr)

            for j in range(K):
                # X cm가 절단된 arr의 길이와 동일하면 안됨
                if j == K-1:
                    # answer.append(cnt)
                    break

                print("j = ", j)
                # print("front arr = ", arr[:j+1])
                # print("middle arr = ", arr[K-(j+1):])
                # rev_val = arr[K-(j+1):]
                # print("reverse mid arr =", rev_val[::-1])

                # 앞 뒤 구조가 일단 대칭이어야, 추가적으로 오색사탕인지 판별할 가치가 있다.
                rev_val = arr[K - (j + 1):]
                if arr[:j+1] == rev_val[::-1]:
                    # 앞 뒤 구조가 대칭이면, 이 때 오색사탕 여부를 체크한다.
                    if arr[:j+1] == rev_val:
                        cnt += 1
                        print("hello")

                # 대칭이 아닐 경우, 더 이상의 탐색은 필요 없다.
                else:
                    # answer.append(cnt)
                    break

            print("cnt = ", cnt)
            answer.append(cnt)
            print("check answer = ", answer)

        if case == 0:
            break

    return answer

#===================================================================================

# 예제 1
candy = "RYRYRGPRYRYRBB"
positions = [12,1,14,7]
print(solution(candy, positions)) # [3,0,0,0]

# 예제 2
candy = "BPBRBPBRB"
positions = [3, 6, 9]
print(solution(candy, positions)) # [1,1,2]


# def solution(candy, positions):
#     answer = []
#     return answer