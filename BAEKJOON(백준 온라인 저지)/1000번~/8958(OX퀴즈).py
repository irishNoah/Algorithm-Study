# 8958 / OX퀴즈 / B2
# https://www.acmicpc.net/problem/8958

# 테스트 케이스 총 개수 변수 case 선언 후 입력 받기
case = int(input())

for i in range(case) :
    # 리스트 변수 test 선언후 각 테스트 케이스 입력
    test = list(map(str, input()))

    # 각 케이스에 대한 총 점수를 구하는 변수 sumValue 선언
    sumValue = 0
    sumValue = int(sumValue)

    # 만약 O에서 X로 만날 경우 연속 점수 부분을 다시 0으로
    # 세팅해주기 위한 변수 setvalue 선언
    setvalue = 0
    setvalue = int(setvalue)

    for j in range(len(test)):
        # O를 만난다면 연속 점수 변수인 setvalue를 1점 증가시키고 이 값을
        # 총 점수를 구하는 변수인 sumValue에 합산
        if test[j] == 'O':
            setvalue += 1
            sumValue += setvalue

        # X를 만난다면 연속 점수 변수인 setvalue를 0점으로 초기화
        elif test[j] == 'X':
            setvalue = 0
    
    print(sumValue)