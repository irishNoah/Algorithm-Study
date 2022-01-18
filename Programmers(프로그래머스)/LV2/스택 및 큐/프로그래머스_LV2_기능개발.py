# 프로그래머스_LV2_기능개발
#https://programmers.co.kr/learn/courses/30/lessons/42586
# https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8A%A4%ED%83%9D%ED%81%90-%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C
import math
def solution(progresses, speeds):
    ans = []
    num = 1
    time = math.ceil((100-progresses[0])/speeds[0])
    for i in range(1, len(progresses)):
        if time >= math.ceil((100-progresses[i])/speeds[i]):
            num += 1
        else:
            ans.append(num)
            num = 1
            time = math.ceil((100-progresses[i])/speeds[i])
    ans.append(num)
    return ans

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))