# 프로그래머스 LV1 - 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(n):
    answer = list(str(int(n)))

    # print(answer)

    answer.sort(reverse=True)


    answer = "".join(answer)

    answer = int(answer)

    return answer

n = 118372
print(solution(n))