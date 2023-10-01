'''
040-[백준]-구현-(스위치-켜고-끄기)-S3-(1-내풀이-IDE정답).py

### 주소
> https://www.acmicpc.net/problem/1244

### 참고
> 다른 사람의 풀이
-

17:15~16:08
### 설계 14분, 총 53분

1. 성별이 남(1)일 때
> [num-1]의 배수의 스위치 값을 toggle
2. 성별이 여(2)일 때
> [num-1]의 배수의 양 옆 값 check
- 단, [num-1]의 인덱스가 0일 때는 > [num-1] 값만 toggle
- 단, [num-1]의 인덱스가 len(num)일 때는 > [num-1] 값만 toggle
- 단, 양 옆이

'''
#===================================================================================

import sys
input = sys.stdin.readline

size = int(input().rstrip())
switch = list(map(str, input().rstrip().split(" ")))
stu = int(input().rstrip())

for _ in range(stu):
    sex, num = input().split()
    sex = int(sex); num = int(num)

    if sex == 1: # 남학생
        step = num-1; base = num
        while step <= len(switch) - 1:
            if switch[step] == "0":
                switch[step] = "1"
            else:
                switch[step] = "0"

            step = step+base


    else: # 여학생
        step = num - 1;

        ### 기준 번호는 일단 토글
        if switch[step] == "0":
            switch[step] = "1"
        else:
            switch[step] = "0"

        # 인덱스 체크하여 토글 진행
        left_idx = step - 1; right_idx = step + 1
        while True:
            if left_idx < 0 or right_idx >= len(switch):
                break
            else:
                if switch[left_idx] == switch[right_idx]:
                    if switch[left_idx] == "0":
                        switch[left_idx] = "1"
                        switch[right_idx] = "1"
                    else:
                        switch[left_idx] = "0"
                        switch[right_idx] = "0"

                    left_idx -= 1
                    right_idx += 1

                else:
                    break

cnt = 0
for idx in range(len(switch)):
    if cnt == 20:
        print()
        cnt = 0
    cnt += 1
    print(switch[idx], end=" ")

#===================================================================================