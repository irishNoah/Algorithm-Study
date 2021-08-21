# (11564번 / 아스키 코드 / B5)

# 값 입력
value = input()

# value의 type이 str이라면 ord() 함수를 통해 아스키 코드 출력
if(str(type(value)) == "<class 'str'>") :
    print(ord(value))

# value의 type이 int라면 chr() 함수를 통해 아스키 코드 출력
else :
    print(chr(value))