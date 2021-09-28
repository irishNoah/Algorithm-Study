# 11655 / ROT13 / B1
# https://www.acmicpc.net/problem/11655

# 풀이 방법 1

# 문자열 입력
value = input()

# for문을 통해 문자열의 각 문자에 대해 ROT13을 구함
# ord() : 해당 문자에 대해 십진수 아스키 코드로 변환해주는 메소드
# > 참고로 A는 10진수 65, Z는 10진수 90, a는 10진수 97, a는 10진수 122에 해당
# > 예 : ord('A') = 65
# chr() : 10진수 아스키 코드에 맞는 문자로 변환
# > 예 : chr(65) = 'A'
for i in value :
    # 만약 i가 ord(i)가 65~90(A~Z) 또는 97~122(a~z) 사이에 있다면 >>> 즉, 영문자라면
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) :
        # 만약 i가 65~77(A~M) 또는 97~109(a~m) 사이에 있다면
        # ord(i)로 반환되는 수에 13을 더한 값을 chr() 메소드를 통해 ROT13를 출력
        if (ord(i) >= 65 and ord(i) < 78) or (ord(i) >= 97 and ord(i) < 110) :
            print(chr(ord(i) + 13), end='')

        # 만약 i가 78~90(N~Z) 또는 110~122(a~z) 사이에 있다면
        # 만약 위 if문 처렴 그냥 13을 더해버리고 chr을 반환하면 영문자가 아닌 다른 문자가 반환되기 때문에
        # ROT13에 맞는 문자를 반환하기 위해서는 오히려 13을 빼줘야 한다.
        elif (ord(i) >= 78 and ord(i) <= 90) or (ord(i) >= 110 and ord(i) <= 122) :
            print(chr(ord(i) - 13), end='')

    # 만약 i가 ord(i)가 65~90(A~Z) 또는 97~122(a~z) 사이에 없다면 >>> 즉, 영문자가 아니라면
    else : 
        print(i, end='')

# ----------------------------------------------------------------------------------
# # 풀이 방법 2

# value = input()
# # res라는 문자열 변수 선언
# res = ''

# for i in value :
#     # 만약 i가 영문자라면
#     if 'a' <= i <= 'z' or 'A' <= i <= 'Z' :
#         # 만약 그 중에서도 a~m 또는 A~M 사이에 있다면
#         if 'a' <= i <= 'm' or 'A' <= i <= 'M' :
#             # ord(i)에 13을 더한 값을 chr()을 통해 영문자로 반환하고 이를 res에 더함
#             res += chr(ord(i) + 13)

#         # 만약 그 중에서도 n~z 또는 N~Z 사이에 있다면
#         elif 'n' <= i <= 'z' or 'N' <= i <= 'Z' :
#             # ord(i)에 13을 뻰 값을 chr()을 통해 영문자로 반환하고 이를 res에 더함
#             res += chr(ord(i) - 13)

#     # 만약 i가 영문자가 아니라면
#     else :
#         # 그냥 그 문자를 res에 더함
#         res += i

# # res 출력
# print(res)