# [프로그래머스]-파이썬-연습문제-(푸드-파이트-대회)-(완주하지-못한-선수)-Hash활용.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건


*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]
- 해시로 접근해서 참여자 명단에 있는 이름값을 기준으로 get()을 활용하여 +1을 해준다.
- 해시로 접근해서 완주자 명단에 있는 이름을 기준으로 -1을 해준다.
- 최종적으로 완주하지 못한 사람의 이름에 해당하는 값은 1이 남을 거기 때문에, 이 값을 리턴해준다.
>>> 해시로 풀게 될 경우 o(n)의 복잡도를 가진다!

*** 참고
https://pydole.tistory.com/entry/Python-collections-Counter%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%95%A9%EC%A7%91%ED%95%A9-%EA%B5%90%EC%A7%91%ED%95%A9-%EC%B0%A8%EC%A7%91%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0
'''
#===================================================================================

def solution(participant, completion):
    d = {}

    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1

    dnf = [k for k,v in d.items() if v > 0]
    answer = dnf[0]
    return answer



#===================================================================================

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["mislav", "stanko", "ana"]

print(solution(participant, completion)) # "mislav"

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# print(solution(participant, completion)) # "leo"

# def solution(participant, completion):
#     answer = ''
#     return answer