# 10989번 / 수 정렬하기 3 / S5
# https://www.acmicpc.net/problem/10989
# 참고 > https://somjang.tistory.com/entry/Mxmxmxm

# 해당 문제는 "수 정렬하기(2750)"와 "수 정렬하기(2751)"과 달리
# 시간 복잡도와 공간 복잡도에 차이가 있다.
# 2750번은 입력값의 범위가 1000, 2751번은 10000000까지이며, 
# 10989번은 10000까지이다.
# 메모지 제한에 있어 2750번은 128MB, 2751번은 256MB이다.
# 그러나 10989번 메모리 제한이 8MB이므로 앞 두 문제에 비해 메모리 제한이
# 더 심해졌다 따라서 input()보다 sys 라이브러리에 있는 sys.stdin.readline()을
# 사용하는 것이 더 좋다.
# ---------------------------------------------------------------
import sys

N = int(input())

check_list = [0] * 10001

for i in range(N) :
    input_num = int(sys.stdin.readline())

    check_list[input_num] = check_list[input_num] + 1

for i in range(10001) :
    if check_list[i] != 0 :
        for j in range(check_list[i]) :
            print(i)