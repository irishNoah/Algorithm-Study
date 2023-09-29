# [프로그래머스]-파이썬-중간고사1번-구현-(상담예약제)-(1-내풀이-25점)-.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 25분 소요] / 총 풀이 시간[총 분 소요]
1. for문을 활용해 booked와 unbooked의 hh:mm 타입을 분(minute) 단위로 치환
> 단, 정수형 변수로 타입을 변경할 것

2. booked과 unbooked의 인덱스를 활용해 진행
> 맨 처음 booked과 unbooked의 0번째 인원의 시간 중 더 빠른 사람이 누구인지 찾기
- 찾으면, 이 사람의 이름을 결과 배열에 담기
- 이 사람의 시간을 변수 check에 할당
3. while문
> booked에서 check 보다 작은 시간이 있다?
- 해당 사람 이름을 결과 배열에 담기
- 이 사람의 시간을 변수 check에 할당

> 만약, booked에서 check 보다 작은 시간이 없다면?
- booked의 남은 인원과 unbooked 인원 중 남은 사람의 시간 따져서 go하기

> 만약, booked나 unbooked에서 남은 사람이 없고 반대쪽만 있다면?
- 남은 사람만 append 하고 끝내면 되지

*** 참고

'''
#===================================================================================

def solution(booked, unbooked):
    answer = []
    # print("=" * 70)

    # 시간 변환
    book = []
    for r in range(len(booked)):
        # print(booked[r][0], booked[r][1])
        time = booked[r][0]
        hour = int(time[:2])
        min = int(time[3:])

        new_time = 60 * hour + min
        book.append([new_time, booked[r][1]])

    unbook = []
    for r in range(len(unbooked)):
        # print(unbooked[r][0], unbooked[r][1])
        time = unbooked[r][0]
        hour = int(time[:2])
        min = int(time[3:])

        new_time = 60 * hour + min
        unbook.append([new_time, unbooked[r][1]])

    # print("book = ", book)
    # print("unbook = ", unbook)

    bookIdx = 0; unbookIdx = 0; check = 0

    # book과 unbook 시간 중에 더 짧은 것 찾기
    if book[bookIdx][0] <= unbook[unbookIdx][0]:
        answer.append(book[bookIdx][1])
        check = book[bookIdx][0]
        bookIdx += 1

    elif book[bookIdx][0] > unbook[unbookIdx][0]:
        answer.append(unbook[unbookIdx][1])
        check = unbook[unbookIdx][0]
        unbookIdx += 1

    while True:
        # 조건1 > 탈출 조건
        if bookIdx == len(book): # unbook에 아직 인원이 있음
            for last in range(unbookIdx, len(unbook)):
                answer.append(unbook[last][1])

            break

        if unbookIdx == len(unbook): # book에 아직 인원이 있음
            # answer.append(book[bookIdx:][1])

            for last in range(bookIdx, len(book)):
                answer.append(book[last][1])

            break

        # 조건 2 > 예약 고객 시간 체크
        if book[bookIdx][0] <= check+600:
            answer.append(book[bookIdx][1])
            check = book[bookIdx][0]
            bookIdx += 1
            continue

        # 조건 3 > 조건2에 해당되지 않은 경우, 일반과 예약 중 무엇이 더 작은지 판별
        if book[bookIdx][0] <= unbook[unbookIdx][0]:
            answer.append(book[bookIdx][1])
            check = book[bookIdx][0]
            bookIdx += 1

        elif book[bookIdx][0] > unbook[unbookIdx][0]:
            answer.append(unbook[unbookIdx][1])
            check = unbook[unbookIdx][0]
            unbookIdx += 1

    return answer

#===================================================================================

# 예제 1
booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"],["09:05", "bae"]]
print(solution(booked, unbooked)) # ["kim", "lee", "bae"]

# 예제 2
booked = [["09:55", "hae"], ["10:05", "jee"]]
unbooked = [["10:04", "hee"],["14:07", "eom"]]
print(solution(booked, unbooked)) # ["hae", "jae", "hee", "eom"]

# def solution(booked, unbooked):
#     answer = []
#     return answer