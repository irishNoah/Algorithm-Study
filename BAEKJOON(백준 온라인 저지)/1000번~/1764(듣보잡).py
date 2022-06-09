# https://github.com/irishNoah/Algorithm-Study
# 1764번 / 듣보잡 / S4
# https://www.acmicpc.net/problem/1764

n, m = map(int, input().split())

# set가 공집합일 경우 {}로 초기화 하는 것이 아니라 set()로 초기화해야 한다.
# 만약 no_hear = {}로 하면 no_hear의 타입은 set가 아니라 dict로 인식하기 때문이다.
# 따라서 {}안에 아무것도 없고, 바로 set 타입으로 할당하기 위해서는
# {}가 아니라 set()로 할당해주어야 한다.
no_hear = set() # 듣도 못한 사람의 집합 no_hear
no_see = set() # 보도 못한 사람의 집합 no_see

# 듣도 못한 사람 명단 입력
while 1:
    value_hear = input()
    no_hear.add(value_hear)
    
    n = n-1

    # while문 탈출 조건
    if n == 0: 
        break

# 보도 못한 사람 명단 입력
while 1:
    value_see = input()
    no_see.add(value_see)
    
    m = m-1

    # while문 탈출 조건
    if m == 0: 
        break

# no_hear & no_see의 교집합이 듣보잡의 집합
# 이를 no_hear_and_see에 할당
no_hear_and_see = no_hear & no_see

# 사전 순으로 출력해야 하므로 no_hear_and_see 오름차순 정렬
no_hear_and_see = sorted(no_hear_and_see)

# no_hear_and_see 길이 출력
print(len(no_hear_and_see))

# for를 활용하여 no_hear_and_see의 각 요소 출력
for value in no_hear_and_see:
    print(value)