# 1676 / 팩토리얼 0의 개수 / S4
# https://www.acmicpc.net/problem/1676

import sys

# 값 입력 받기
n = int(sys.stdin.readline())

# 기본적으로 0이 나오게 하려면 무조건 5가 필요하다.
# 따라서 0의 개수를 파악하려면 입력받은 값의 팩토리알의 곱 중에서
# 5가 몇 개 있냐에 따라 0의 개수가 달라지는 것이다.
# 입력받는 범위는 0 <= n <= 500 이다.
# 고려해야 하는 부분은 5의 n승일때라는 것이다.
# 500 이하의 수 중에서 5의 n승에 해당되는 부분은 5, 25, 125가 있다.
# 따라서 아래 print()문에 나온 것처럼 3개 부분에 대해 더한 것을 출력해주면 된다.
print(n//5 + n//25 + n//125)

# ----------------------------------------------------------------------
# 처음에는 입력받은 값에 대해 실제로 팩토리알 값을 구해보았다.
# 그 다음 while문을 통해 팩토리알 값에서 0이 아닌 다른 수를 만나기 전까지
# 일일이 나머지 값을 구하면서 나머지 값이 0이면 0의 개수를 1씩 증가하는 식으로 구했다.
# VS CODE 내에서는 실제로 이렇게 해서 풀어도 답은 잘 나왔다.
# 하지만 답 제출 때 overflow가 나왔는데, 문제에서 보면 n의 가장 큰 입력 값은 500인데
# 500!을 구해보면 이 팩토리알의 자릿수만 보더라도 무려 528이다.
# 즉, 시스템 상 이걸 2초안에 풀지는 못하기 때문에 이 방식은 틀린 방식이었다.