/*
010-[프로그래머스]-SELECT-(여러-기준으로-정렬하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59404

### 참고
> 없음

*** 08:52~08:53
### 설계 1분, 총 1분

*/

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC;