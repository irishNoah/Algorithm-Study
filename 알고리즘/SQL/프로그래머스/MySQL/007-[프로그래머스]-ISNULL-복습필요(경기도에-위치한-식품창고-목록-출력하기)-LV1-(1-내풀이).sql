/*
007-[프로그래머스]-ISNULL-복습필요(경기도에-위치한-식품창고-목록-출력하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131114

### 참고
> 없음

*** 22:42~22:47
### 설계 2분, 총 5분
> IFNULL의 형식
    - IFNULL(컬럼명, 대체값) AS '프린트속성명'
        - 특정 컬렴명에 위치하는 값이 NULL일 경우에 대체값을 할당
    - IFNULL이 어디에 위치하는지 파악할 것
*/

-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS 'FREEZER_YN'
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID