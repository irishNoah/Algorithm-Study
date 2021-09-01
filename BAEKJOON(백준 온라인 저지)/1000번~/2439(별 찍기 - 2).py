# 2439 / 별 찍기 - 2 / B3
# https://www.acmicpc.net/problem/2439

# 줄의 개수 입력
n = int(input())

for i in range(1, n+1):
    # 한 줄에 * 이 몇 개 들어갈건지를
    # index 변수인 i의 값을 활용하여 정함
    star = '*' * (i)
    
    # rjust() 오른쪽 정렬 / center() 가운데 정렬 / ljust() 왼쪽 정렬
    # 문제에서는 오른쪽 정렬이므로 rjust()를 활용한다.
    print(star.rjust(n))