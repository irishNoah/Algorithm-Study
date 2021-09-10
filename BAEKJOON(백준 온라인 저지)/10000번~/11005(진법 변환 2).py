# 11005 / 진법 변환 2 / B1
# https://www.acmicpc.net/problem/11005

import string

# tmp에 대문자를 다 넣었기 때문에 16진법 이상도 가능
tmp = string.digits+string.ascii_uppercase

# 함수 convert 구현
# num이 10진수 base가 앞의 10진수를 해당 진수로 바꾸고 싶은 진수 대입
def convert(num, base) :
    # 몫과 나머지를 구하는 메소드 divmod() 사용
    q, r = divmod(num, base)

    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

n, b = map(int, input().split())

print(convert(n, b))