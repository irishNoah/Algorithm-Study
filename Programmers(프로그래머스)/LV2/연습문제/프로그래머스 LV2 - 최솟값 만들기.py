# 프로그래머스 LV2 - 최솟값 만들기
# 분류 - 연습문제
# https://programmers.co.kr/learn/courses/30/lessons/12941

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트의 케이스 4개 중 4개 성공
# 총점 100.0

def solution(A,B):
    answer = 0

    '''
    A를 오름차순 정렬하여 sort_A에 할당
    B를 오름차순 정렬하여 sort_B에 할당
    '''
    sort_A = sorted(A, reverse=False)
    sort_B = sorted(B, reverse=True)

    '''
    zip()을 이용하여 sort_A와 sort_B의 값을 
    차례대로 곱한 값은 answer에 할당
    '''
    for i, j in zip(sort_A, sort_B):
        answer += i * j

    # answer 리턴
    return answer


A = [1, 4, 2]	
B = [5, 4, 4]	

print(solution(A,B)) # 결과 예 : 29