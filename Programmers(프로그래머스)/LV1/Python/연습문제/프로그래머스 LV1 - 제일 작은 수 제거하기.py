# 프로그래머스 LV1 - 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(arr):
    # arr의 길이가 1 이하라면 arr에 [-1]를 대입
    if len(arr) <= 1 :
        arr = [-1]

    # arr의 길이가 1보다 크다면 arr에 [-1]를 대입
    else :
        # arr 요소 중 최소값 요소를 찾고 이를 min_value에 대입
        min_value = min(arr)        

        # min_value 값을 갔는 요소를 제거
        arr.remove(min_value)

    # 리스트 arr 제거
    return arr

arr = [10]
print(solution(arr))