# 9093 / 단어 뒤집기 / B1
# https://www.acmicpc.net/problem/9093

# 테스트케이스에 대한 변수 test 입력 받기
test = int(input())

# stack 자료 구조를 이용하여 풀기
for i in range (test) :
    # 단어 입력
    value = input()
    # 단어 중간중간 마다 공백이 포함되어 있는데
    # 이 공백 역시 입력 받아주는 것으로 정함
    value += " "

    # stack 변수 선언, 여기에 리스트 할당
    stack = []
    

    for j in value :
        # 단어 중간중간에 공백이 있는데 value에서 공백 전의 단어에 대해서
        # 뒤집어주어야 하기 때문에 공백을 만나기 전까지 그 단어를
        # stack에 append()를 통해서 추가
        if j != " " :
            stack.append(j)
        
        # 공백을 만나면 stack이 빌 때까지 pop을 통해서 출력
        else :
            while stack :                
                print(stack.pop(), end='')
            print(' ', end='')

    print()