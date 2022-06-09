# https://github.com/irishNoah/Algorithm-Study
# 1427번 / 소트인사이드 / S5
# https://www.acmicpc.net/problem/1427

# 자연수 num 입력
num = int(input())

# num을 str 타입으로 변형 후 num을 리스트화
str_num_list = list(str(num))

str_num_list.sort() # 오름차순 정렬
str_num_list.reverse() # 내림차순 정렬
print(''.join(str_num_list)) # 출력