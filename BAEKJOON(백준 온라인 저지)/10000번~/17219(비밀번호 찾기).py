# https://github.com/irishNoah/Algorithm-Study
# 17219번 / 비밀번호 찾기 / S4
# https://www.acmicpc.net/problem/17219

n, m = map(int, input().split())

# 각 사이트 주소와, 사이트 주소에 해당하는 비밀번호를 기억하기 위한 딕셔너리 변수 dict_site 생성
dict_site = dict()

# 찾고자 하는 사이트 주소를 입력했을 때, 이 사이트 주소에 맞는 비밀번호가 무엇인지 기억하기 위한
# 리스트 변수 find_site 생성
find_site = []

while 1: # while문 0번
    while 1: # while문 1번
        # 사이트명과 비밀번호를 공백으로 구분하여 입력
        input_site, input_pw = map(str, input().split())

        # 딕셔너리에 삽입
        dict_site[input_site] = input_pw

        n = n-1 # while문 돌 때마다 n은 1 감소

        if n == 0: # while문 1번 탈출 조건
            break

    while 1: # while문 2번
        # 비밀번호를 찾고자 하는 사이트명 입력
        input_site = input()

        # 비밀번호를 딕셔너리를 이용해 찾기
        find_pw = dict_site[input_site]

        # 찾은 비밀번호를 리스트 find_site에 append() 하기
        find_site.append(find_pw)

        m = m-1 # while문 돌 때마다 m은 1 감소

        if m == 0: # while문 2번 탈출 조건
            break

    # while문 1번, 2번이 끝나면 0번은 그냥 조건 없이 탈출
    break

# 찾은 비밀번호 for문 활용해 출력하기
for value in find_site:
    print(value)