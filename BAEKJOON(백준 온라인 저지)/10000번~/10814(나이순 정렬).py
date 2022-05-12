# https://github.com/irishNoah/Algorithm-Study
# 10814번 / 나이순 정렬 / S5
# https://www.acmicpc.net/problem/10814

# 참고 : https://wook-2124.tistory.com/481

n = int(input())

ls = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    ls.append((age, name))

# sort_ls = sorted(ls) -> A-Z 순으로 정렬되서 오답처리 됨

ls.sort(key=lambda parameter_list:parameter_list[0])

'''
위 lamda 식과 동일
ls 안에 있는 것들에 parameter_list의 인수(argument)가 되어
인덱스 [0]에 해당되는 age로만 정렬됨
인덱스 [1]로 하면 name으로 정렬할 것임

def lamda(parameter_list):
    return parameter_list[0]
'''

for i in ls:
    print(i[0], i[1])