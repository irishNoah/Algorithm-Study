/*
042-[프로그래머스]-STRING&DATE-(대여 기록이 존재하는 자동차 리스트 구하기)-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/157341

### 참고
>

*** 23:56 ~ :
### 내 설계 7분, 총 분

###### 설계
> 조회
- CAR_ID >>> 중복 제거
> FROM(조인)
- CAR C INNER JOIN HISTORY H ON C.CAR_ID = H.CAR_ID
    - ON ID
> WHERE 
- C.CAR_TYPE = '세단' AND MONTH(시작일) = 10
> 정렬
- CAR_ID DESC


*/

-- 코드를 입력하세요
SELECT  DISTINCT(C.CAR_ID)
FROM    CAR_RENTAL_COMPANY_CAR C 
        INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        ON C.CAR_ID = H.CAR_ID
WHERE   C.CAR_TYPE = '세단'
        AND MONTH(H.START_DATE) = 10
ORDER   BY C.CAR_ID DESC;