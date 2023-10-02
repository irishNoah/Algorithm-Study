'''
041-[백준]-구현-복습필요(크로스-컨트리)-S4-(1-내풀이-IDE정답).py

### 주소
> https://www.acmicpc.net/problem/9017

### 참고
> https://itstime0809.tistory.com/4
-

16:05~16:
### 설계 분, 총 분
> for문을 돌면서
- 각 값을 기준
    - 딕셔너리(info)에 있는 키일 경우
        - info[val].append(인덱스)
    - 없는 경우
        - info[val] = list()
        - info[val].append(인덱스)

> for문을 돌면서
    - len(info[key])


'''
#===================================================================================
t = int(input())
for _ in range(t):
    n = int(input())
    count = {}  # 팀 당 주자 수
    temp = list(map(int, input().split()))

    # 팀 별로 주자 수 세기
    for i in range(n):
        if temp[i] in count:
            count[temp[i]] += 1
        else:
            count[temp[i]] = 1

    # 제외되는 팀 구하기
    dele = {}  # 제외되는 팀
    for k, v in count.items():
        if v < 6:
            dele[k] = 1

    # 점수 계산
    team = {}
    idx = 1  # 점수
    for i in range(n):
        if temp[i] not in dele:
            if temp[i] in team:
                if team[temp[i]][0] < 4:
                    team[temp[i]][0] += 1
                    team[temp[i]][1] += idx
                elif team[temp[i]][0] == 4:
                    team[temp[i]][0] += 1
                    team[temp[i]][2] = idx
            else:
                team[temp[i]] = [1, idx, 0]  # [팀당 주자 수, 상위 4명 점수 합, 5번째 주자의 점수]

            idx += 1

    # 순위 정렬
    team = sorted(team.items(), key=lambda x: (x[1][1], x[1][2]))
    print(team[0][0])
#===================================================================================