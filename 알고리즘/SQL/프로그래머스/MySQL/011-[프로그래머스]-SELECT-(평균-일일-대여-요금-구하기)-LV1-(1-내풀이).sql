/*
011-[프로그래머스]-SELECT-(평균-일일-대여-요금-구하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/151136

### 참고
> https://velog.io/@donghoim/MySQL-SQL-ROUND-FLOOR-CEIL-%ED%95%A8%EC%88%98

*** 08:54~08:58
### 설계 2분, 총 4분
> 소수점 n번째 자리에서 반올림을 하고 싶다면?
- ROUND(숫자, N-1)


*/

-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE),0) AS 'AVERAGE_FEE' FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'