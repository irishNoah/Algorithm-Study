# 프로그래머스 LV2 - 이진 변환 반복하기
# 분류 - 월간 코드 챌린지 시즌1
# https://programmers.co.kr/learn/courses/30/lessons/70129

# 정확성 테스트의 케이스 11개 중 11개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(s):
    answer = []

    # 이진 변환 횟수를 파악하기 위한 변수 cnt_binary
    cnt_binary = 0

    # 각 회차마다 s에 존재하는 0의 갯수를 파악하기 위한 변수 cnt_zero
    cnt_zero = 0

    while 1:
        # while문 종료 조건
        if s == "1":
            break

        # while문이 종료가 안된다면 cnt 1 증가
        cnt_binary += 1

        # s에 존재하는 "0"의 갯수를 파악한 후, 이를 cnt_zero에 더해줌
        cnt_zero += s.count("0")

        # 각 회차마다 s에 존재하는 0을 제거하기 위해 replace() 메소드 활용
        s = s.replace("0", "")

        # s에 존재하는 1의 갯수가 len(s)와 동일하며, 이를 len_s 변수에 할당
        len_s = len(s)

        # len_s를 2진수로 변환한 값을 다시 s에 대입
        s = bin(len_s)[2:]

    # while문이 종료되고 최종적으로 구해진 cnt_binary, cnt_zero를 answer에 할당
    answer.append(cnt_binary)
    answer.append(cnt_zero)

    return answer


s = "110010101001"

print(solution(s)) # 결과 예 : [3,8]