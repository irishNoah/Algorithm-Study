/*
001-[프로그래머스]-SELECT-(인기있는-아이스크림)-LV1-(1-내풀이).sql
### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/133024

### 설계 1분, 총 2분

*/

-- 코드를 입력하세요
SELECT FLAVOR 
FROM FIRST_HALF 
ORDER BY TOTAL_ORDER DESC, 
SHIPMENT_ID;