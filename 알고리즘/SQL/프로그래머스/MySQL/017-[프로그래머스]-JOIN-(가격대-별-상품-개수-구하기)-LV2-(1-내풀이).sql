/*
017-[프로그래머스]-JOIN-(가격대-별-상품-개수-구하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/144854

### 참고

*** 19:52~20:01
### 설계 3분, 총  분
> 도서 ID(BOOK), 저자명(AUTHOUR), 출판일(BOOK)
    -출판일의 데이트 형식
        - DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d")
> 두 테이블 간의 공통키로 JOIN
- AUTHOR_ID
> 책 카테고리 = '경제'
> 출판일을 기준으로 ASC

*/

-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, "%Y-%m-%d") AS 'PUBLISHED_DATE'
FROM BOOK B JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY B.PUBLISHED_DATE ASC;