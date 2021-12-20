def solution(new_id):
    # 1단계 : 대문자를 모두 소문자로 변경
    idCntList = new_id.lower()

    # 2단계 : 소문자,숫자, 빼기(-),밑줄(_), 마침표(.)를 제외한 모든 문자 제거

    # 문자열 answer 선언
    answer = ''

    # for문을 통해서 소문자, 숫자, 빼기, 밑줄, 마침표를 가진 요소의 값에 대해서만 
    # checkChar를 통해 판별하고 만약 그 값을 갖고 있다면 answer 집어넣기
    for i in range(0, idCntList.__len__()):
        checkChar = idCntList[i]

        # islower()은 소문자인지 판별하는 메소드
        # isdigit()은 숫자인지 판별하는 메소드
        if checkChar.islower() or checkChar.isdigit() or checkChar == '-' or checkChar == '_' or checkChar == '.' :
            answer += checkChar

    # 3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환하기
    while(True) :
        if ".." in answer :
            answer = answer.replace("..", ".", len(answer))
        else :
            break

    # 4단계 : 마침표(.)가 처음이나 끝에 위치한다면 제거한다.
    answer = answer.strip(".")

    # 5단계 : 빈 문자열이면, "a"를 대입
    if answer == "" : 
        answer = "a"

    # 6단계 : 문자열의 길이가 16 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if answer.__len__() >= 16 :
        answer = answer[0:15]
    # 단, 6단계이후 15번째의 값이 마침표(.)일 경우에는 4단계에 걸리므로
    # 여기서도 마침표가 마지막에 온다면 제거해준다.
    answer = answer.strip(".")

    # 7단계 : 문자열의 길이가 2 이하라면, 문자열의 마지막 문자를
    # 문자열의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while(True):
        if len(answer) <= 2:
            answer += answer[-1]
        else : 
            break

    return answer