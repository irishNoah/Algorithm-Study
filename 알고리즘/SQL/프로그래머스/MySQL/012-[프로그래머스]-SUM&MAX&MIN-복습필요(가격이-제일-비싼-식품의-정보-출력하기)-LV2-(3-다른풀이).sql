/*
012-[프로그래머스]-SUM&MAX&MIN-복습필요(가격이-제일-비싼-식품의-정보-출력하기)-LV2-(3-다른풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131115

### 참고
> 없음

*** 08:14~08:
### 설계 분, 총 분

*/

-- 코드를 입력하세요
SELECT *
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);
