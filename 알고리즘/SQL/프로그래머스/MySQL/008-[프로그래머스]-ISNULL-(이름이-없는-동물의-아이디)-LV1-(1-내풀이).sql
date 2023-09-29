/*
008-[프로그래머스]-ISNULL-(이름이-없는-동물의-아이디)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59039

### 참고
> 없음

*** 22:52~22:54
### 설계 1분, 총 2분

*/

-- 코드를 입력하세요
SELECT ANIMAL_ID 
FROM ANIMAL_INS
WHERE NAME IS NULL;