# 프로그래머스 LV1 - 나머지가 1이 되는 수 찾기(초기 풀이)
# 분류 - 월간 코드 챌리지 시즌 3
# https://programmers.co.kr/learn/courses/30/lessons/87389

# 정확성 테스트의 케이스 0개 중 0개 성공
# 효율성 테스트는 없었음
# 총점 0.0

'''
이 문제는 소수를 이용하여 문제를 해결하고자 했다.
주어진 숫자가 n일 때 n이하의 모든 소수를 판별하고
n을 n 이하의 소수로 나눴을 때 나머지가 1이 나올 수 있게 하는 모든 소수 중
가장 작은 소수가 나올 수 있도록 하기 위해서
primePy 라이브러리의 primes를 import 하려고 했었다.
프로그로밍 상에는 문제가 발생하지 않았으나, 해당 문제를 프로그래머스 내에서
코드 실행을 하면 

Traceback (most recent call last):
  File "/solution_test.py", line 6, in <module>
    from solution import *
  File "/solution.py", line 3, in <module>
    from primePy import primes
ModuleNotFoundError: No module named 'primePy'

와 같은 메시지가 출력됐다.

따라서 이 방식은 프로그래머스 상에서는 적합하지는 않았다.

그러나 primePy 라이브러리라는 존재를 알게 된 것에 만족한다.
'''

from primePy import primes

def solution(n):
    answer = 0 # 리턴할 값 answer

    primes_to_n = primes.upto(n)
    # print("11111")
    print(primes_to_n)
    # print("22222")


    for i in primes_to_n:
        if n % i == 1:
            # print("33333")
            print(i)
            # print("44444")            
            answer = i
            break

    return answer

n = 10
print(solution(n)) # 출력 예 : 3