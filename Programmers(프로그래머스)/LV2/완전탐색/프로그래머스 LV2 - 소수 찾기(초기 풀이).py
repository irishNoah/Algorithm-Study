# 프로그래머스 LV2 - 소수 찾기(초기 풀이)
# 분류 - 완전탐색
# https://programmers.co.kr/learn/courses/30/lessons/42839

# 정확성 테스트의 케이스 12개 중 9개 성공
# 효율성 테스트는 없었음
# 총점 75.0

from itertools import permutations
import math

def solution(numbers):
    answer = 0
    # numbers를 나누어서 split_numbers에 대입
    # numbers가 "012"라면 split_numbers는 ['0', '1', '2']
    split_numbers = list(numbers)

    '''
    split_numbers에서 "0" 또는 중복된 값은 불필요하게 밑에 나오는 list_all에 할당할 필요는 없으므로
    아래 3개 라인을 통해서 먼저 split_numbers에서 "0"을 제거해주고
    중복된 값을 제거한 것을 before_process에 대입한다.
    '''
    remove_set = {'0'}
    before_process = list(dict.fromkeys([i for i in split_numbers if i not in remove_set]))

    
    list_all = before_process

    '''
        i가 0이 아니라면 permutations_CK라는 변수에
        차례대로 n개씩 조합의 수를 구해준다.
        또한 조합으로 이루어진다면 중복된 경우가 발생할 수 있으므로 dict.formkeys()를 통해
        중복된 값을 제거한다.
        그러고 나서 리스트 내의 튜플을 모두 리스트 형식으로 바꾸어 주기 위해 
        [list(x) for x in permutations_CK]를 실행한다. > 참고 : https://blog.finxter.com/how-to-convert-list-of-tuples-to-list-of-lists-in-python/
    '''
    for i in range(2, len(split_numbers)+1):
        permutations_CK = list(dict.fromkeys((list(permutations(numbers, i)))))

        for j in range(0, len(permutations_CK)):
            permutations_CK[j] = ''.join(permutations_CK[j])

            if permutations_CK[j][0] == "0":
                permutations_CK[j] = permutations_CK[j][1:]

            if permutations_CK[j] not in list_all:
                list_all.append(permutations_CK[j])


    # 문자열 숫자로 이루어진 list_all을 map() 함수를 사용해 정수 숫자로 변환
    list_all = list(map(int, list_all))

    '''
    소수 판별
    만약 i가 1개라도 성립되는 게 있다면 소수가 아니고,
    모두 다 성립되지 않는다면 해당 수는 소수임
    '''
    for i in range(0, len(list_all)):
        check_prime = 0

        if list_all[i] == 0 or list_all[i] == 1:
            continue

        for j in range(2, int(math.sqrt(list_all[i])) + 1):
            if list_all[i] % j == 0:
                check_prime += 1
                break

        if check_prime == 0:
            answer += 1

    return answer

numbers = "17"

print(solution(numbers)) # 결과 예 : 3