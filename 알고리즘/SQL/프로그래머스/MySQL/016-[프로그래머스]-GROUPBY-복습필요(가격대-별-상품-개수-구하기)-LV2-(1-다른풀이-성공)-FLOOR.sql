/*
016-[프로그래머스]-GROUPBY-복습필요(가격대-별-상품-개수-구하기)-LV2-(1-다른풀이-성공)-FLOOR.sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131530

### 참고
> https://devwarriorjungi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-131530-MySQL-Level2-%EA%B0%80%EA%B2%A9%EB%8C%80-%EB%B3%84-%EC%83%81%ED%92%88-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0

*** 10:05~10:??
### 설계 분, 총 분


*/

-- 코드를 입력하세요
SELECT FLOOR(PRICE / 10000) * 10000 AS `PRICE_GROUP`, 
    COUNT(*) AS PRODUCTS
    FROM PRODUCT
GROUP BY `PRICE_GROUP`
ORDER BY `PRICE_GROUP`;