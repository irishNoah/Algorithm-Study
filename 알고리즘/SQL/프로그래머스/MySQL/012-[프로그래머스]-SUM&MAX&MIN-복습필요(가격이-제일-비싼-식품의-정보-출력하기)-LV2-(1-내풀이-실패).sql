/*
012-[프로그래머스]-SUM&MAX&MIN-복습필요(가격이-제일-비싼-식품의-정보-출력하기)-LV2-(1-내풀이-실패).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131115

### 참고
> 없음

*** 08:14~08:
### 설계 분, 총 분
> 풀이 2, 3과 비교해본다면...
난 정렬이나 WHERE 조건 절에서 내부 SELECT를 활용하지 않아서 그런감..?

*/

-- 코드를 입력하세요
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, MAX(PRICE) AS 'PRICE'
FROM FOOD_PRODUCT
LIMIT 1;
