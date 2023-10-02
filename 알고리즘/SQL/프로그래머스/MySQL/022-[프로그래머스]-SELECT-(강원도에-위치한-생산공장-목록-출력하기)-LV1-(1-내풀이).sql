/*
022-[프로그래머스]-SELECT-(강원도에-위치한-생산공장-목록-출력하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131112

### 참고
> 없음

*** 08:47~08:48
### 설계 1분, 총 분


*/

-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID;