# 10820 / 문자열 분석 / B2
# https://www.acmicpc.net/problem/10820

import sys

while True :
    # 한줄씩 입력될 때마다 자동적으로 엔터가 들어간다.
    # 엔터도 컴퓨터상에서 공백으로 인지할 수 있기 때문에 
    # 엔터 같은 경우는 입력에서 제외하라고 지시를 해주기 위해
    # rstrip() 메소드를 사용했다.
    value = sys.stdin.readline().rstrip('\n')

    s_under = 0
    s_upper = 0
    s_num = 0
    s_space = 0

    if not value :
        break

    # 파이썬 메소드를 활용하여 소문자, 대문자, 숫자, 공백의 숫자를 구하였다.
    for i in value :
        if i.islower() :
            s_under += 1

        elif i.isupper() :
            s_upper += 1

        elif i.isdigit() :
            s_num += 1

        elif i.isspace() :
            s_space += 1

    sys.stdout.write("{} {} {} {}\n".format(s_under, s_upper, s_num, s_space))