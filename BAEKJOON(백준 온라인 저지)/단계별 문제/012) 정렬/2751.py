# 2751번 / 수 정렬하기 2 / S5
# https://www.acmicpc.net/problem/2751
# 해당 문제는 백준에서 pypy3로 정답 제출함

# 해당 문제는 "수 정렬하기(2750)"번과 출력 결과는 동일하게 나오더라도
# 시간 복잡도에 차이가 있다. 2750번은 입력값의 범위가 1000까지로
# 시간 복잡도가 O(N*N)이다.
# 그러나 2751번은 입력값의 범위가 1000000(백만)까지로 시간 복잡도는
# O(NlogN)에 해당된다. 따라서 이 시간 복잡도 내에 풀기 위해서는
# 고급 정렬 알고리즘(병합 정렬, 퀵 정렬, 힙 정렬 등)을 이용하거나
# 기본 정렬 라이브러리를 이용해서 풀어야만 한다.
# ---------------------------------------------------------------

# 병합 정렬 함수 구현
def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

# 데이터 입력
n=int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)