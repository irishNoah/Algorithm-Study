# 프로그래머스 LV2 - 전화번호 목록(zip()과 stratswith())
# https://programmers.co.kr/learn/courses/30/lessons/42577
# 참고[zip()] : https://www.daleseo.com/python-zip/
# 참고[startswith()] : https://security-nanglam.tistory.com/429

# 정확성 테스트의 케이스 19개 중 19개 성공
# 효율성 테스트의 케이스 4개 중 4개 성공 
# 총점 100.0점

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
            return answer
    return answer

phone_book = ["123","456","789"]
print(solution(phone_book))