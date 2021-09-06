# 1978 / 소수 찾기 / S4
# https://www.acmicpc.net/problem/1978

# 명령의 개수 n 입력
n = int(input())

# n개의 수를 map() 형식으로 arr 변수에 할당
arr = map(int, input().split())

# 주어진 수들 중에 소수가 몇 개인지 구하기 위한 변수 count 선언
count = 0

# arr 안에 있는 각각의 수가 소수인지 아닌지 판별함
for num in arr :
    # num마다 약수의 개수를 구하기 위한 변수 yaksoo 선언
    yaksoo = 0

    # 애초에 2 이상의 숫자부터 소수인지 아닌지만 보면 되므로
    # 입력받은 수가 1에 해당되면 걍 건너뛰면 됨
    if num > 1 :
        # 2부터 num-1까지 비교
        for i in range(2, num) :
            # 만약 2부터 num-1까지의 수중에 나머지를 구할시 0이 나오면
            # 그 수는 소수가 아님 
            if num % i == 0:
                yaksoo += 1
        
        # 바로 위 for문에서 구한 yaksoo의 수가 0일 때에만 소수이므로
        # yaksoo가 0이라면 count 증가
        if yaksoo == 0:
           count += 1

# count 출력
print(count) 