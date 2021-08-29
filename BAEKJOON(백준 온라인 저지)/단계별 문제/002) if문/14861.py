# 14861 / 사분면 고르기 / B4
# https://www.acmicpc.net/problem/14681

# x 좌표와 y 좌표 입력 받기
x = input()
y = input()

x = int(x)
y = int(y)


# 파이썬 if 문에서는 &&, || 등의 기호가 아닌 
# and, or처럼 문자로 쓰면 된다.
if x > 0 and y > 0 :
    print(1)

elif x < 0 and y > 0 :
    print(2)

elif x < 0 and y < 0 :
    print(3)

elif x > 0 and y < 0 :
    print(4)