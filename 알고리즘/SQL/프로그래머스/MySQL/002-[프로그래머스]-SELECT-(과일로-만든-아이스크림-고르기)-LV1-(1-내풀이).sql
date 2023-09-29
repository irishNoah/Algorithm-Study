/*
002-[프로그래머스]-SELECT-(과일로-만든-아이스크림-고르기)-LV1-(1-내풀이).sql
### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/133025

*** 16:55~17:05
### 설계 6분, 총 10분

*/

-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF F, ICECREAM_INFO I
WHERE F.FLAVOR = I.FLAVOR
AND F.TOTAL_ORDER > 3000
AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;