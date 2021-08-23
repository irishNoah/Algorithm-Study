# 2675 / 문자열 반복 / B2
# https://www.acmicpc.net/problem/2675

# 시간 초과 판정이 나지 않게 하기 위해 input()으로 입력받는 것이 아닌
# sys.stdin.readline()을 통해 입력을 받고자 sys를 import한다.
import sys

# 명령의 수 test
test = int(sys.stdin.readline())


convert1 = []
convert2 = []
for i in range(test) :
    value = 0
    command = sys.stdin.readline().split()

    #list(리스트 변수명)을 넣어주면 공백 포함 한 문자씩 분해해줌
    # 예 : 리스트 변수명 - hi / hi의 값 = "work"
    # list(hi) > ['w', 'o', 'r', 'k']
    case = list(command[1])

    for j in range(len(command[1])) :
        for k in range(int(command[0])) :
            convert1.append(case[j])
    
    # ('').join(리스트 변수명) 해주면 한 리스트에 있는 구분자들을  한꺼번에 합쳐
    # 한 단어로 만들어준다.
    value = ('').join(convert1)
    convert2.append(value)
    # clear() 메소드를 통해 convert1의 모든 요소들을 지워준다.
    convert1.clear()

for i in range(test) :
    print(convert2[i])