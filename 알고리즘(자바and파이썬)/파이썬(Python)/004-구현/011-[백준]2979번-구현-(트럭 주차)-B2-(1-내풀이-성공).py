# [백준]2979번-구현-(트럭 주차)-B2-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2979

'''
# 문제 풀이

1. 각 차의 도착시간, 떠난 시간 입력 받는다.
2. 각 차에 대해 컴프리헨션을 활용하여 리스트 생성 후, 이를 set()로 타입을 변환한다.
3. 집합자료형을 활용해 교집합, 합집합, 차집합 등을 차례대로 구한다.
4. 구한 집합을 토대로 값을 구한다.
'''

import sys

a, b, c = map(int, sys.stdin.readline().split())

# 각 차 도착시간, 떠난 시간 입력
s1, f1 = map(int, sys.stdin.readline().split())
s2, f2 = map(int, sys.stdin.readline().split())
s3, f3 = map(int, sys.stdin.readline().split())

# 여기서 컴프리헨션 사용할 때 range() 값의 마지막을 f1+1이 아닌 f1으로 해야 한다.
# 그렇게 해야 올바른 정답이 도출되기 때문이다.
car1 = [i for i in range(s1, f1)]; car1 = set(car1)
car2 = [i for i in range(s2, f2)]; car2 = set(car2)
car3 = [i for i in range(s3, f3)]; car3 = set(car3)

# 순수 car1, car2, car3만 구하기
sumA =  (car1-(car2|car3)) | (car2-(car1|car3)) | (car3-(car1|car2))

# car1, car2, car3 전체 교집합 구하기
sumC = (car1 & car2 & car3)

# 차 2대씩 교집한 것에서 전체 교집합 뺀 것만 구하기
sumB = (((car1 & car2) - sumC) | ((car2 & car3) - sumC) | ((car1 & car3) - sumC))

value = (len(sumA))*a + (len(sumB))*b*2 + (len(sumC))*c*3
print(value)