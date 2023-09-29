2. # [백준]2852-구현-(NBA농구)-S3-(2-참고-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2852

'''
# 문제 풀이

1. 48분을 포함하여 입력된 모든 분과 초 개념을 초로 전환해서 계산하는 법!
2. flag 값이 0일 경우 비기는 case
3. flag 값이 양의 정수 > 1팀이 이기고 있는 상황
4. flag 값이 음의 정수 > 2팀이 이기고 있는 상황


'''
n = int(input())

one_time = 0 # 1번팀이 이기는 시간
two_time = 0 # 2번팀이 이기는 시간
flag = 0

for i in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    
    if team == '1': # 입력된 팀 번호가 1일 때 
        if flag == 0:  # 이제 이기려고 함
            one_time += 48 * 60 - (60 * m + s)
            
        flag += 1
        
        if flag == 0: # 이걸 넣으면 비겨.
            if two_time > 0:
                two_time = two_time - (48 * 60 - (60 * m + s))
                
    else: # 입력된 팀 번호가 2일 때 
        if flag == 0:  # 이제 이기려고 함
            two_time += 48 * 60 - (60 * m + s)
            
        flag -= 1
        
        if flag == 0:  # 이걸 넣으면 비겨.
            if one_time > 0:
                one_time = one_time - (48 * 60 - (60 * m + s))

print('{:0>2}:{:0>2}'.format(one_time // 60, one_time % 60))
print('{:0>2}:{:0>2}'.format(two_time // 60, two_time % 60))
