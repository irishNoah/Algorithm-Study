# 프로그래머스 LV2 - 행렬의 곱셈
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12949

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0

'''
행렬이라는 말은 들어본 적은 있지만 행렬의 곱의 원리가
어떻게 작용되는지는 몰라서 인터넷을 검색한 후 
행렬의 곱을 구하는 방식을 파악했다.

기본적으로 arr1이 만약 m * n의 사이즈이고,
arr2가 만약 a * b의 사이즈라고 가정한다면
두 행렬의 곱 결과 사이즈는 m * b이다.
'''

def solution(arr1, arr2):
    # 리턴할 값 answer의 크기를 먼저 지정해줌
    answer = [ len(arr2[0])*[0] for i in range (len(arr1)) ]
    
    for i in range (len(answer)):
        for j in range (len(answer[i])):
            for k in range (len(arr1[i])):
                answer[i][j] += arr1[i][k]*arr2[k][j]

    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2)) # 결과 예 : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]