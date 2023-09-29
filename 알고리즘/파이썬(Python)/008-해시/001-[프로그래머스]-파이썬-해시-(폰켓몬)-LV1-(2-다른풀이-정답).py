# [프로그래머스]-파이썬-해시-(폰켓몬)-LV1-(2-다른풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건
nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.

* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

'''
#===================================================================================

'''
참고 >>> https://latte-is-horse.tistory.com/101

아이디어는 다음과 같다.
N / 2마리를 뽑는다고 했을 때 각자 다른 포켓몬이면 N / 2 종류의 포켓몬이 선택될 것이다.
그러나 중복 포켓몬이 많아서 N / 2 마리보다 적은 종류라면 그 종류 수 만큼이 선택할 수 있는 최대 종류의 수가 될 것이다.

choose에 nums를 2로 나눠서 N / 2 마리를 계산했고
set을 통해 nums 리스트의 중복을 없앴다.

둘 중 더 적은 수가 답이 되므로 min 함수로 답을 찾을 수 있었다.
'''
def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return int(unique_types)
    else:
        return int(len(nums) / 2)

# #############################################################

nums = [3,3,3,2,2,2]
print(solution(nums))