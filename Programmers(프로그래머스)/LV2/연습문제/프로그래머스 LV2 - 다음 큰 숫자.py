# 프로그래머스 LV2 - 다음 큰 숫자
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12911

# 정확성 테스트의 케이스 14개 중 14개 성공
# 효율성 테스트의 케이스 6개 중 6개 성공
# 총점 100.0

def solution(n):
    answer = 0


    # n을 이진수로 변환한 후, 이진수 n의 1의 개수를 파악하귀 위한 변수 cnt_one_bin_n
    cnt_one_bin_n_1 = bin(n).count('1')

    while 1:
        # n+1부터 차례대로 비교
        n = n + 1

        # n+1을 이진수로 변환한 후, 이진수 n의 1의 개수를 파악하귀 위한 변수 cnt_one_bin_n_2
        cnt_one_bin_n_2 = bin(n).count('1')

        # cnt_one_bin_n_2와 cnt_one_bin_n_1이 동일할 경우 해당 if문 수행
        if cnt_one_bin_n_2 == cnt_one_bin_n_1:
            # answer에 n 대입
            answer = n

            # while문 탈출
            break

    return answer

n = 15
print(solution(n)) # 결과 예 : 23