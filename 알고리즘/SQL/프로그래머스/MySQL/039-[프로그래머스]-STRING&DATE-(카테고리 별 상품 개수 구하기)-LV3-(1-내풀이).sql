/*
039-[프로그래머스]-STRING&DATE-(카테고리 별 상품 개수 구하기)-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131113

### 참고
>

*** 11:48 ~ 11:54
### 내 설계 3분, 총 6분
> OUT_DATE를 기준으로 출고여부를 CASE 구문을 활용해 구분한다.
    - 5월 1일 이하의 날 >>> 출고완료
    - 5월 1일 이후의 날 >>> 출고대기
    - NULL >>> 출고미정

*/

-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") AS "OUT_DATE",
    CASE
        WHEN DATE_FORMAT(OUT_DATE, "%Y-%m-%d") <= "2022-05-01"
            THEN "출고완료"
        WHEN DATE_FORMAT(OUT_DATE, "%Y-%m-%d") > "2022-05-01"
            THEN "출고대기"
        WHEN OUT_DATE IS NULL
            THEN "출고미정"
    END AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC;