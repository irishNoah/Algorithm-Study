/*
025-[프로그래머스]-GROUPBY-(카테고리-별-도서-판매량-집계하기)-LV3-(1-내풀이-정답).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/144855

### 참고
> 없음

*** 09:18~09:28
### 설계 5분, 총 10분
> 조회
- CATEGORY, SUM(SALES)
> 조인(INNER JOIN)
- BOOK B / BOOK_SALES S
- ON B.BOOK_ID = S.BOOK_ID
> WHERE
- 판매일의 연도 = 2022 / 월 = 1
> GROUP BY
- 카테고리
> ORDER BY
- 카테고리 ASC

*/

-- 코드를 입력하세요
SELECT B.CATEGORY, SUM(S.SALES) AS 'TOTAL_SALES'
FROM BOOK B INNER JOIN BOOK_SALES S
ON B.BOOK_ID = S.BOOK_ID
WHERE YEAR(S.SALES_DATE) = 2022 AND MONTH(S.SALES_DATE) = 1
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC;