# https://github.com/irishNoah/Algorithm-Study
# 2947번 / 나무 조각 / S5
# https://www.acmicpc.net/problem/2947

num_list = list(map(int, input().split())) # 리스트 입력

while_break = 0 # while문 탈출 조건 변수

while 1:
    for i in range(0, 4):
        # 각 차수에서 조건에 충족하면 i번째 요소의 값과 i+1번째 요소의 값을 swap
        if num_list[i] > num_list[i+1]:
            temp = num_list[i+1]
            num_list[i+1] = num_list[i]
            num_list[i] = temp

            # 바꾸어질 때마다 num_list 출력
            for j in range(len(num_list)):
                print(num_list[j], end=' ')


            # for문 탈출 조건
            if num_list == [1,2,3,4,5]:
                # for문 탈출 조건이 부합할 경우 while문 탈출 조건 변수를 1로 할당
                while_break = 1
                break # for문 탈출

            else: # for문 탈출 조건에 부합하지 않을 경우 다음 줄로 커서 이동
                print()
        
    if while_break == 1: # while문 탈출 조건
        break