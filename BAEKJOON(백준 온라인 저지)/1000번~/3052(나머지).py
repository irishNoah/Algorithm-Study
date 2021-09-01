# 3052 / 나머지 / B2
# https://www.acmicpc.net/problem/3052

# 나머지 중에서 중복되지 않은 값만 저장하는 나머지 리스트 check 선언
check = []
for i in range(10):
    # 숫자 입력
    value = int(input())
    # 각 숫자에 대해 42로 나눈 나머지를 구하는 변수 remain
    remain = int(value % 42)

    # 리스트 check의 값들 중에 만약 remain이 없으면(즉, 중복된 값이 없으면)
    # 이 remain 값에 대해서는 check에 append() 해준다.
    if not remain in check :
        check.append(remain)

# 최종적인 check 리스트의 길이를 출력한다.
print(len(check))