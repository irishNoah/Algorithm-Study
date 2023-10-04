/*
035-[프로그래머스]-STRING&DATE-(이름에 el이 들어가는 동물 찾기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59047

### 참고
>

*** 11:10 ~ 11:13
### 내 설계 1분, 총 3분


*/

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC;