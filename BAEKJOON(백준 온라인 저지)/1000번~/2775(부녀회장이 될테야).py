# https://github.com/irishNoah/Algorithm-Study
# 2775번 / 부녀회장이 될테야 / B1
# https://www.acmicpc.net/problem/2775

# Test case의 수 T 입력
T = int(input())

while 1:
    # while문 탈출 조건
    if T == 0:
        break

    # 층에 대한 변수 k 입력
    k = int(input())

    # 호에 대한 변수 n 입력
    n = int(input())

    '''
    2차원 리스트 layer_zero 생성
    참고로 layer_zero에 들어간 리스트 값 1~14는
    아파트가 0충부터 시작하고, 각 호가 최대 14이하이므로
    아파트 0층 각 호수의 거주 인원 수를 차례대로 넣은 것이다.
    '''
    layer_zero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    '''
    문제에서 원하는 것은 n호에 거주하는 인원을 파악하는 것이므로 
    굳이 n호 이후에 있는 거주 인원을 파악할 필요성이 없다.

    이에 따라 layer_zero에 있는 n호까지의 인원만 파악해서 arr_real에 대입한다.

    참고로 문제에서는 1호부터 시작한다고 했으나 실제 인덱스는 0부터 시작하기 때문에
    0~(n-1)까지 범위의 인덱스만 대입한다. 
    '''
    arr_real = layer_zero[0:n]

    # 0층은 이미 layer_zero에 할당되어 있으므로 층에 대한 시작은 1부터 수행하도록 한다.
    for i in range(1, k+1):
        # 추후에 arr_real에 convert_arr를 할당하고자 미리 선언
        convert_arr = []

        # 문제에서는 호가 1호부터 존재한다고 하나 리스트의 인덱스는 0부터 접근하므로 0부터 (n-1)까지 for문 수행하도록 한다.
        for j in range(0, n):
            # arr_real에서 0부터 j까지의 합을 value에 할당한다.
            value = sum(arr_real[0:j+1])

            # value를 convert_arr에 append한다.
            convert_arr.append(value)

        # 최종적으로 구해진 convert_arr를 arr_real에 대입한다.
        arr_real = convert_arr

    # 최종적으로 구해진 k층의 n호 값을 출력한다.
    print(arr_real[n-1])

    # 한 횟수가 끝날 시 T를 1 감소
    T = T - 1