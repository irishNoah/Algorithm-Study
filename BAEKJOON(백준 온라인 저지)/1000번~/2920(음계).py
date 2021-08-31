# 2920 / 음계 / B2
# https://www.acmicpc.net/problem/2920

# 8개 숫자 입력 받기
music = list(map(int, input().split()))

# 1부터 8까지 오름차순 정렬되어 있는 list인 test 선언
test = [1, 2, 3, 4, 5, 6, 7, 8]
# 8부터 1까지 내림차순 정렬되어 있는 list인 test2 선언
test2 = [8, 7, 6, 5, 4, 3, 2, 1]

# music이 오름차순 정렬되어 있는 test와 값이 모두 같다면 
# ascending 출력
if music == test :
    print("ascending")

# music이 오름차순 정렬되어 있는 test와 값이 모두 같다면 
# ascending 출력
elif music == test2 :
    print("descending")

# 위 두 가지 경우에 해당하지 않는다면 
# mixed 출력
else :
    print("mixed")