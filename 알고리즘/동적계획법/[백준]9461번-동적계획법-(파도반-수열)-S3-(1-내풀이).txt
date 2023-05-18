# [백준]9461번-동적계획법-(파도반-수열)-S3-(1-내풀이)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9461

# n[i]의 값을 구하기 위한 사용자 정의 함수 samkag
def samkag(val):
    if 0 <= val <= 5:
        return n[val]
    
    # n[val] 값 구하기
    for i in range(6, val+1): 
        # n[i]의 값의 점화식은 아래와 같음
        n[i] = n[i-1] + n[i-5]

    return n[val]


t = int(input()) # 테스트케이스 개수 변수 t

n = [0] * 101 # 각 정삼각형의 한 변의 길이에 대한 정보를 담은 리스트 n

# n[1]부터 n[5]까지에 대한 정보를 담음
n[0] = 0; n[1] = 1; n[2] = 1; n[3] = 1; n[4] = 2; n[5] = 2

cnt = 0 # while문을 몇 번 들었는지 확인하기

while True:
    cnt += 1

    val = int(input()) 

    print(samkag(val))

    if cnt == t: # while문 탈출 조건
        break