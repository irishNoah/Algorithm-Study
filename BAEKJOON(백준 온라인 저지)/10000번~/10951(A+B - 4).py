# 10951 / A+B - 4 / B3
# https://www.acmicpc.net/problem/10951

# 이 문제는 테스트케이스의 개수가 명시되어 있지 않으므로
# 언제까지 입력을 받을 줄 모른다.
# 따라서 try - except문을 활용해야 하는데
# error에 해당되지 않으면 try문을, error에 해당되면 except문을 실행한다.
while True :
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break