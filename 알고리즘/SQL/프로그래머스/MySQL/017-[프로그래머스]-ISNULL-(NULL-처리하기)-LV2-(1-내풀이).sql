/*
017-[프로그래머스]-ISNULL-(NULL-처리하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59410

### 참고
> 없음

*** 09:26~09:32
### 설계 1분, 총 6분

*/


-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS 'NAME', SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;