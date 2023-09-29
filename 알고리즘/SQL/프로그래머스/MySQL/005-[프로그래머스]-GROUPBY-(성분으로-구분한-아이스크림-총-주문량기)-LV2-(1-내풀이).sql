/*
005-[프로그래머스]-GROUPBY-(성분으로-구분한-아이스크림-총-주문량기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/133026

*** 22:14~22:23
### 설계 6분, 총 9분

*/

-- 코드를 입력하세요
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS 'TOTAL_ORDER'
FROM FIRST_HALF F, ICECREAM_INFO I
WHERE F.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY SUM(F.TOTAL_ORDER);







