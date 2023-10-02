/*
029-[프로그래머스]-STRING&DATE-(특정 옵션이 포함된 자동차 리스트 구하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/157343

### 참고
> 

*** 20:24~:
### 내 설계 분, 총 분
> 

*/

-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;