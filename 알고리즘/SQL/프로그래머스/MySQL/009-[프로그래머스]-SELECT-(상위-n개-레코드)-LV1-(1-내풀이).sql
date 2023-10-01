/*
009-[프로그래머스]-SELECT-(상위-n개-레코드)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59405

### 참고
> 없음

*** 08:45~08:49
### 설계 1분, 총 4분
> 집계 함수(SUM/AVG/MIN/MAX) 등은 SELECT 절과 함께 써야 하지
WHERE절에 쓰면 안된다.

*/

-- 코드를 입력하세요
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1;