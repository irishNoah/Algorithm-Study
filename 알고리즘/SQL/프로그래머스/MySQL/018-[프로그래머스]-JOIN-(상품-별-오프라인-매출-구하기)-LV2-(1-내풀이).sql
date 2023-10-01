/*
018-[프로그래머스]-JOIN-(상품-별-오프라인-매출-구하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131533

### 참고

*** 20:04~20:14
### 설계 8분, 총 10분
> 검색 : P.PRODUCT_CODE, SALES
- PRODUCT 테이블(P) / OFFLINE_SALE(O)
- PRODUCT_CODE는 PRODUCT 테이블
- SALES > SUM(O.SALES_AMOUNT) * P.PRICE AS SALES
> 조인
- 조인 기준 : PRODUCT_ID
> 그룹핑
- 키 : PRODUCT_ID
> 정렬
- 2 DESC, 1 ASC
    - 2가 매출액 / 1이 상품코드

*/


-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, SUM(O.SALES_AMOUNT) * P.PRICE AS SALES
FROM PRODUCT P JOIN OFFLINE_SALE O
ON P.PRODUCT_ID = O.PRODUCT_ID 
GROUP BY O.PRODUCT_ID
ORDER BY 2 DESC, 1 ASC;