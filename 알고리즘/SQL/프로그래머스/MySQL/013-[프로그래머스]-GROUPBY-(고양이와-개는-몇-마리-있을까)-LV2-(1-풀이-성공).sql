/*
013-[프로그래머스]-GROUPBY-(고양이와-개는-몇-마리-있을까)-LV2-(1-풀이-성공).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59040

### 참고
> 없음

*** 09:51~09:54
### 설계 1분, 총 3분


*/

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS 'count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;