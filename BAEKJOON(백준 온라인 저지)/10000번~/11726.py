# 백준 11726 - 2 x n 타일링(다이나믹 프로그래밍)
# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 
# 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 
# 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 2
# 예제 입력 2 
# 9
# 예제 출력 2 
# 55

# -------------------------------------------------------------

# 문제 푼 방법
# 우선 2*n크기의 직사각형을 1*2, 2*1 타일로 채워야 할 때,
# X*Y 타일이라고 한다면, 여기서 X는 세로, Y는 가로를 의미한다.

# 1) 1*2 타일은 하나로는 직사각형을 채울 수 없다. 
# 최소 2개가 있어야 직사각형을 채울 수 있다.
# 2) 2*1 타일은 하나로 직사각형을 채울 수 있다.

# > 여기서 1*2 타일 2개를 이제 하나로 간주하며 
#   1*2 타일 2개짜리를 A로 가정한다.
# > 2*1 타일 1개를 하나로 간주하며
#   1*2 타일 1개짜리를 B로 가정한다.

# 1. 만약 n=3이라면
# B3, B1+A1 이 2가지 방식으로 직사각형을 채울 수 있는데,
# B1+A1의 경우에는 순서를 바꾸어서 채울 수 있으므로, 
# 이에 대한 경우의 수는 2개이다.
# 따라서 n=3일 때 결과값은 3이다.

# 2. 만약 n=4라면
# A2, B4, A1+B2 이 3가지 방식으로 직사각형을 채울 수 있는데,
# A1+B2의 경우에는 순서를 바꾸어서 채울 수 있으므로, 
# 이에 대한 경우의 수는 3개이다.
# 따라서 n=4일 때 결과값은 5이다.

# 3. 만약 n=5라면
# B5, A2+B1, A1+B3 이 3가지 방식으로 직사각형을 채울 수 있는데,
# A2+B1의 경우에는 순서를 바꾸어서 채울 수 있으므로, 
# 이에 대한 경우의 수는 3개이다.
# A1+B3의 경우에는 순서를 바꾸어서 채울 수 있으므로, 
# 이에 대한 경우의 수는 4개이다.
# 따라서 n=5일 때 결과값은 8이다.

# & "A2+B3의 경우에는 순서를 바꾸어서 채울 수 있으므로 이에 대한 경우의 수는 4개이다."
# 라는 문장에서 A와 B 각각 뒤에 있는 숫자를 x,y라고 해보자.
# 즉 Ax, By가 되는 것이다.
# 이렇게 Ax, By가 한 번에 계산되는 경우의 수는 다음과 같다.
# (x+y)! / (x)! * (y)! [@여기서 !는 팩토리얼을 의미한다.]
# 즉, 예를 들어 A1+B3 경우에는
# 4! / 1! * 3! = 4 이런 식으로 되는 것이다.

# & 이제 n에 대한 각각의 결과 값을 알아보자
# n = 1,2,3,4,5 일 때 각각의 결과값은 1,2,3,5,8이다.
# 이를 통해 알 수 있는 것은 각각의 결과값이 피보나치 식으로 나온다는 
# 것을 알 수 있다.

#-------------------------------------------------

# 2*n 크기에서 n 입력받기
n = int(input())

# n을 입력했을 때 결과값은 피보나치에 해당하는 값으로
# 우선 n이 1과 2일 때의 결과 값을 
# 리스트 listFibo에 넣어준다.
listFibo = [1, 2]

sum = 0

for i in range(2, n+1) :
    # sum이라는 변수에 listFibo[i-1]와 
    # listFibo[i-2]번째를 더한 값을 넣어준다.
    sum = listFibo[i-1] + listFibo[i-2] 
    # sum을 lisftFibo에 append 한다.
    listFibo.append(sum)

# 결과값을 출력해준다.
print(listFibo[n-1] % 10007)