# [백준]9461번-동적계획법-(파도반-수열)-S3-(2-다른분풀이)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9461

wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1

for i in range(4, 101):
    wh[i] = wh[i-2] + wh[i-3]

t = int(input())

for i in range(t):
    n = int(input())
    print(wh[n])

'''
* 코드 성능 차이
- 내 코드보다 4ms만 차이 났다. >>> 즉, 별 차이 없다.
- 대신 코드 길이가 훨씬 간단. >>> 나는 약 1200B, 이것은 약 190B
- 즉, 이 코드가 좀 더 좋은 코드!!!

* 나와 다르게 푼 점

1. 나와 점화식을 다르게 해서 풀었다. >>> 이 분이 세운 점화식이 더 간단
2. 나는 사용자 정의 함수를 사용해서 풀었지만, 이것이 중요한 것이 아니다.
나는 각 n의 입력값마다 메모리를 아껴 보겠다고 for문 안에서 n+1 까지만 구하고
답을 출력하게 했다.
하지만, n의 범위 값이 매우 큰 값이 아니고, for문이 1차이기 때문에
어차피 시간 복잡도가 o(n)이다.
따라서, 범위 값이 매우 높은 것이 아니라면 복잡하게 생각할 필요 없이
모든 리스트 값을 다 구하는 게 더 풀이 시간을 단축하는 방식에 해당한다고 할 수 있다.

'''