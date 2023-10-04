/*
037-[프로그래머스]-STRING&DATE-(DATETIME에서 DATE로 형 변환)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59414

### 참고
>

*** 11:28 ~ 11:29
### 내 설계 0분, 총 1분

*/

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    DATE_FORMAT(DATETIME, "%Y-%m-%d") AS "날짜"
FROM ANIMAL_INS;