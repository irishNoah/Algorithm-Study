/*
036-[프로그래머스]-STRING&DATE-(중성화 여부 파악하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59409

### 참고
>

*** 11:14 ~ 11:19
### 내 설계 1분, 총 5분
>>> LKIK는 OR가 안된다!!!

*/

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
    
