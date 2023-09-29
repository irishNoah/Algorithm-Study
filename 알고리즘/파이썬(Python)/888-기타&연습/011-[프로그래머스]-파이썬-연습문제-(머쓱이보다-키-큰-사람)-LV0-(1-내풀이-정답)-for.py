# [프로그래머스]-파이썬-연습문제-(머쓱이보다-키-큰-사람)-LV0-(1-내풀이-정답)-for.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120585

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 8분 소요]
- array 리스트 길이가 100이하이기 때문에 시간 복잡도는 O(N^3)까지 가능
- array 오름차순 정렬
- for
    - array[i]가 height보다 작거나 같?
        - cnt += 1
    - 그렇지 않다?
        - break
- return len(array)-cnt

*** 참고

'''
#===================================================================================

def solution(array, height):

    array.sort()
    cnt = 0
    for tall in array:
        if tall < height:
           cnt += 1
        else:
            break

    return len(array)-cnt


#===================================================================================

# 예제 1
array = [149, 180, 192, 170]
height = 167
print(solution(array, height)) # 3

# 예제 2
array = [180, 120, 140]
height = 190
print(solution(array, height)) # 0

# def solution(array, height):
#     answer = 0
#     return answer
