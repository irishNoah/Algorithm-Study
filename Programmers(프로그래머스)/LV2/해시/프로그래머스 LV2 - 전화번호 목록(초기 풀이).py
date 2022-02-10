# 프로그래머스 LV2 - 전화번호 목록(초기 풀이)
# https://programmers.co.kr/learn/courses/30/lessons/42577

# 정확성 테스트의 케이스 19개 중 16개 성공 3개 실패
# 효율성 테스트의 케이스 4개 중 3개 성공 1개 실패
# 총점 83.3점(정확성 70.8 + 효율성 12.5)


# def solution(phone_book):
#     answer = True
#     return answer

def solution(phone_book):
    answer = True # return할 값 answer

    # 문자열 숫자를 크기로 인식하여 정렬하기
    phone_book.sort(key = int)

    # 맨 첫 번째에 있는 수가 가장 작은 수에 해당된다.
    # 이에 따라 맨 앞에 있는 수의 길이 만큼 그 뒤에 있는 수를 비교한다.
    # 만약 맨 앞에 있는 수가 다른 수의 접두어로 존재한다면 아래 for문은 중지하고 false를 반환하게 한다.
    # 만약 맨 앞에 있는 수가 다른 모든 수의 접두어로 존재하지 않는다면 맨 앞에 있는 수는 pop()을 시행한다.
    # 만약 계속 pop()을 통해 리스트의 길이가 1일 경우 더 이상 비교할 것이 없으므로 for문을 중지하고 true를 반환한다.
    for i in range(1, len(phone_book)):

        if phone_book[i][0:len(phone_book[0])] == phone_book[0] :
            answer = False
            break

        if i == len(phone_book)-1 :
            # phone_book 리스트의 길이가 1일 경우 비교할 대상이 없으므로 for문을 탈출한다.
            if len(phone_book) == 1:
                break

            else :
                phone_book.pop(0)


    return answer

phone_book = ["123","456","789"]
print(solution(phone_book))
