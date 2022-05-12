# 프로그래머스 LV1 - 소수 만들기
# 분류 - 위클리 챌린지
# https://programmers.co.kr/learn/courses/30/lessons/12977

# 정확성 테스트의 케이스 26개 중 26개 성공
# 효율성 테스트는 없었음
# 총점 100.0

'''
iterools에 대한 참고 링크 : https://yganalyst.github.io/etc/memo_18_itertools/

해당 문제는 itertools를 활용하여 풀었다.
특히 itertools의 combinations 메소드를 이용했다.
참고로 combinations 메소드는 중복조합을 사용할 때 쓰인다.

해당 문제는 주어진 리스트에서 3개의 수를 뽑아 이 3수를 더한 값이
소수인지 아닌지에 따라 결과값이 달라진다.

단순 조합일 경우 1, 2, 3 이렇게 3개의 수를 뽑았을 때
이것만 해도 조합의 수가 8개나 된다.
그러나 문제는 중복된 값도 일일이 count하는 것을 요구하는 것이 아니므로
순서만 다를 뿐 결과는 동일한 조합은 필요 없으므로 중복 조합을 활용하는 것이다.
'''

import itertools
import math

def solution(nums):
    # nums에서 3개의 수를 뽑아 중복 조합한 경우의 리스트를 담은 list_permutations
    list_permutations = list(itertools.combinations(nums,3))

    # 조합 안에서의 합이 소수일 경우 이 합을 담을 리스트 store_sum_list
    store_sum_list = []

    '''
    리스트 list_permutations를 for문으로 돌면서
    각 중복 조합 요소를 sum_value 변수에 합산하여 할당한다.

    check_prime은 sum_value가 소수인지 아닌지를 판별하기 위해 선언했다.

    만약 check_prime이 1이 되는 순간 sum_value는 소수가 아니므로
    안에 있는 for문을 break를 통해 탈출하며, 최종적으로 sum_value가 소수일 경우
    sum_value를 store_sum_list에 append 해주었다.

    최종적으로 구한 store_sum_list의 길이를 리턴해준다.
    '''
    for value in list_permutations:
        sum_value = sum(value)
       
        check_prime = 0       

        for i in range(2, int(math.sqrt(sum_value) + 1)):
            if sum_value % i == 0:
                check_prime += 1

            if check_prime == 1:
                break
        
        if check_prime == 0:
            store_sum_list.append(sum_value)

    return len(store_sum_list)

nums = [1,2,7,6,4]		
print(solution(nums)) # 출력 예 : 4