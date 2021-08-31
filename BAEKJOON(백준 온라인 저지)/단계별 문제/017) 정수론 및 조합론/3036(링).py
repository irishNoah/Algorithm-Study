# 3036 / 링 / S3
# https://www.acmicpc.net/problem/3036

# 출력 형태를 소수가 아닌 분수로 하기 위해 
# fraction 모듈의 Fraction 객체를 import한다.
# 참고로 Fraction 객체는 기약분수 형태로 알아서 변환해준다.
from fractions import Fraction

# 테스트 케이스의 개수 입력
testCase = int(input())

ring = list(map(int, input().split()))

for i in range(testCase-1):
    # res라는 변수에 기약 분수의 형태롤 넣어준다.
    res = Fraction(ring[0], ring[i+1])

    # 기약분수가 2/1과 같은 형식이라면 res의 출력은 그냥 2가 된다.
    # 하지만 문제에서 요구하는 것은 2/1과 같이 분모가 1인 경우에도 출력되는 것을 원하므로
    # Fraction 객체에서 분자를 추출하는 메소드인 numerator과
    # 분모를 추출하는 메소드인 denominator를 사용한다면 분모가 1인 경우에도
    # 온전히 출력할 수 있다.
    print(f'{res.numerator}/{res.denominator}')