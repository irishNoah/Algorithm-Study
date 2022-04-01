# https://github.com/irishNoah/Algorithm-Study
# 1259번 / 팰린드롬수 / B1
# https://www.acmicpc.net/problem/1259

while 1:
    # 입력한 정수를 변수 num에 대입
    num = int(input())

    # while문 종료 조건
    if num == 0:
        break

    # num을 문자열로 치환한 후 list화 하기
    list_num = list(str(num))

    # 문자열 변수 asnwer 선언
    answer = ""

    # len(list_num)이 홀수일 경우
    if len(list_num) % 2 == 1:
        # 가운데 수는 굳이 비교해볼 필요성은 없으므로 가운데 요소 값 제거
        list_num.pop(int((len(list_num)-1) /2))

        # for문을 돌면서 차레대로 앞 값과, 이 앞 값에 대칭되는 뒷 값과 비교
        # 만약 이 두 값이 동일한 값이 아니라면 answer에 no를 대입 후 for문 탈출
        for i in range(0, int(len(list_num)/2)):
            if list_num[i] != list_num[len(list_num)-(i+1)]:
                answer = "no"
                break
        
        # answer가 "no"일 경우 answer 바로 출력
        if answer == "no":
            print(answer)

        # answer가 "no"가 아닐 경우 answer에 "yes" 대입 후 이를 출력
        else:
            answer = "yes"
            print(answer)

    # len(list_num)이 짝수일 경우
    # elif문 내에 있는 코드들은 위 if믄 안에 있는 내용 맥락과 동일하므로 주석 생략
    elif len(list_num) % 2 == 0: 
        for i in range(0, int((len(list_num)/2))):
            if list_num[i] != list_num[len(list_num)-(i+1)]:
                answer = "no"
                break
        
        if answer == "no":
            print(answer)

        else:
            answer = "yes"
            print(answer)