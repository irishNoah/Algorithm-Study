# 프로그래머스 LV2 - N개의 최소공배수
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12953

# 정확성 테스트의 케이스 10개 중 10개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(arr):
    # 재귀 호출 recursive_sol 종료 조건
    if len(arr) == 1:
        answer = arr[0]
        return answer

    # 최소공배수 구하기
    for i in range(max(arr[0], arr[1]), (arr[0]*arr[1])+1):
        if i % arr[0] == 0 and i % arr[1] ==- 0:
            '''
            최소공배수인 i는 arr의 맨 마지막에 append 해주고
            최소공배수를 구하려고 사용했던 arr[0]과 arr[1]의 값들은
            arr.pop(0)을 2번 해줌으로써 제거해주기
            '''
            arr.pop(0)
            arr.pop(0)
            arr.append(i)
            break

    # 자기 자신 return 하기
    return solution(arr)
    

arr = [2,6,8,14]
print(solution(arr)) # 결과 예시 : 168