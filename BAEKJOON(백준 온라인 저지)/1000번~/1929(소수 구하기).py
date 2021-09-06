# 1929 / 소수 구하기 / S2
# https://www.acmicpc.net/problem/1929

# 명령의 개수 n 입력
a, b = map(int, input().split())

# 모든 수마다 2부터 자기 자신의 수까지 검사하면 컴퓨터 시간상 너무 오래 걸린다.
# 2부터 자기 자신의 수의 제곱근까지만 검사하면 그 이후는 검사할 필요성이 없어진다.
# 이를 함수로 구현하면 다음과 같다.
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

# for문 안에서 위의 함수를 호출하면 된다.
for i in range(a, b+1):
    if isPrime(i):
        print(i)