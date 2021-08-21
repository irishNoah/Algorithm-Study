# 2941번 / 크로아티아 알파벳 / S5
# https://www.acmicpc.net/problem/2941

# 크로아티아 문자열 단어 입력
test = input()

# 단어가 알파벳 소문자와 '-', '='로만 이루어진다 나와있기 때문에
# 크로아티아 알파벳을 차례대로 replace() 함수를 통해 숫자로 변경
test = test.replace("c=", "1")
test = test.replace("c-", "2")
test = test.replace("dz=", "3")
test = test.replace("d-", "4")
test = test.replace("lj", "5")
test = test.replace("nj", "6")
test = test.replace("s=", "7")
test = test.replace("z=", "8")

# 바꾼 단어에 대한 길이를 구함
print(len(test))