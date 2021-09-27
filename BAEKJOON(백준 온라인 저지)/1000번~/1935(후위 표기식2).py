# 1935 / 후위 표기식2 / S3
# https://www.acmicpc.net/problem/1935

# 피연산자의 개수 value 선언 및 입력
n = int(input())

# 후위 표기식 리스트 value 선언 및 입력
value = list(input())

# 각 알파벳에 대한 값 리스트 alpha_value 선언 및 입력 받기
alpha_value = [int(input()) for i in range(n)]

# 후위 표기식에 대한 리스트 postfix_Notation 선언
postfix_Notation = []

# 피연산자냐 연산자냐에 따라 for문을 통해 아래와 같이 수행함
for i in value :
    # 만약 value 내에서 알파벳이면, 
    # 알파벳에 대한 각 아스키 코드 값을 나타내는 ord() 함수를 통해 그 값을 구하고
    # 알파벳 A에 해당되는 아스키 코드값 65를 뺀 값이 결국에는 alpha_value의 값에 해당 되므로
    # 이 값을 postfix_Notation 리스트에 추가
    if i.isalpha() == True :
        postfix_Notation.append(alpha_value[ord(i)-65])

    # 만약 value 내에서 알파벳이 아니라면 다음과 같은 for문 실행
    else :
        num = postfix_Notation.pop()
        result = postfix_Notation.pop()

        if i == '+':
            result += num

        elif i == '-' :
            result -= num

        elif i == '*' :
            result *= num

        elif i == '/' :
            result /= num

        postfix_Notation.append(result)

# 소수 둘 째 자리까지 출력
print("%.2f" %postfix_Notation[-1])