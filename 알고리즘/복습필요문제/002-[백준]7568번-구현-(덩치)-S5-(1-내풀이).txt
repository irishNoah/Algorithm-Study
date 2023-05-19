# [백준]7568번-구현-(덩치)-S5-(1-내풀이)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/7568

n = int(input()) # 사람수 n 입력

weigh = []; tall = []

# 각 사람에 대한 몸무게와 키 입력
for _ in range(n):
    x, y = map(int, input().split()) # 몸무게 x, 키 y 입력

    weigh.append(x); tall.append(y);

# 각 사람에 대한 등수 구하기
for i in range(n):
    cnt = 1 # 큰 for문마다 등수에 대한 변수 cnt를 1로 초기화

    for j in range(n):
        # 몸무게와 키 모두 작아야 등수가 밀려남
        if weigh[i] < weigh[j] and tall[i] < tall[j]:
            cnt += 1

    print(cnt, end=" ")

'''
1. 처음에는 weigh[i] < weigh[j] and tall[i] < tall[j]가 아닌
weigh[i] > weigh[j] and tall[i] > tall[j]를 구해서
cnt를 증가 시키고 나서, 여기서 구해진 값을 뒤집어서 랭크를 계산하려고 하다보니
복잡해졌다.
2. 애초에 몸무게와 키 모두 작아야 등수가 밀려난다는 원리를 구했다면 좋았을 것 같다.
'''