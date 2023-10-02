/*
024-[프로그래머스]-SELECT-(조건에-맞는-도서-리스트-출력하기)-LV1-(1-내풀이-정답).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/144853

### 참고
> 없음

*** 09:12~09:16
### 설계 1분, 총 4분

*/


-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d")
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021 AND CATEGORY = "인문"
ORDER BY PUBLISHED_DATE ASC;