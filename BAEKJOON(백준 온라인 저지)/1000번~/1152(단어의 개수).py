# 1152 / 단어의 개수 / B2
# https://www.acmicpc.net/problem/1152

# 문자열 입력받기
a = input()
# 공백을 기준으로 단어를 나누어 각각 리스트 b에 저장하기
b = a.split()
# b의 길이가 곧 단어의 개수를 의미하므로 b의 길이를 출력하기
print(len(b))