# 2884 / 알람 시계 / B3
# https://www.acmicpc.net/problem/2884

# 시와 분 입력 받기
hour, min = map(int, input().split())

# 1) 분이 45분 이상이라면 기존 분에서 45분 뺏을 때 분이 0 이상이므로
# 시 자체가 1시간 떨어질 일이 없다.
if min >= 45 :
    min = min - 45
    print("{0} {1}".format(hour, min))

# 2) 분이 45분 미만이라면 기존 분에서 45분 뺏을 때 기본 적으로 0 이만인데다가
# 분이 최대 60분이라는 것 역시 감안해야 하며, 시간도 1시간 차감된다는 것을 생각해야 한다.
elif min < 45 :
    # min이 40분이라면 45분을 뺏을 때 55분이 되어야 한다. 
    # 따라서 45분과 min의 차이가 60분과 (45분과 min의 차이)를 뺀 것과 동일하므로
    # 아래 2줄의 코드를 삽입한다.
    min = 45 - min
    min = 60 - min

    # 또한 hour가 1 이상이면 상관 없으나 hour가 0이면 -1을 할 시
    # hour를 23으로 변경을 해주어야 한다.
    if hour == 0 :
        hour = 23

    # hour가 1 이상이면 아래 코드를 수행한다.
    else :
        hour = hour-1 

    # 출력
    print("{0} {1}".format(hour, min))