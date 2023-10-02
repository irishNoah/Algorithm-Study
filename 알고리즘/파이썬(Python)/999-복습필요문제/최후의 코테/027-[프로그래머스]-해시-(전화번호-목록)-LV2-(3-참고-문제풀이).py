'''
027-[프로그래머스]-해시-(전화번호-목록)-LV2-(3-참고-문제풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42577

### 참고
> https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%8B%9C-%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D

# 15:30~ 15:54
### 설계 5분, 총 24분
> phoneBook 들어간 숫자는 int 타입이 아니라 string 타입이다.
> 따라서 phoneBook을 정렬하면, 내가 아는 일반적인 정수의 순으로 정렬되는 것이 아니라
- 앞의 숫자가 무엇이냐에 따라 정렬이 된다! >>> 즉, 일단 비슷한 구성끼리 최대한 정렬이 된다는 것!
- 따라서, phoneBook이 정렬된 상태에서
zip(phoneBook, phoneBook[1:])을 해줄 경우, 
[값1, 값2] / [값2, 값3] ... 이런 식으로 매칭이 이루어진다.
그래서 가장 비슷한 매칭에서 (값N)이 (값N+1)의 접두어로 시작하는지만 판별하면 된다.

'''

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    # print("sorted(phoneBook) = ", phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        # print("p1 = ", p1, " p2 = ", p2)
        
        if p2.startswith(p1):
            return False
    return True