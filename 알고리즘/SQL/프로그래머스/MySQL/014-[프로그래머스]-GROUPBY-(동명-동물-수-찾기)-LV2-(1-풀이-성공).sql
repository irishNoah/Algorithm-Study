/*
014-[프로그래머스]-GROUPBY-(동명-동물-수-찾기)-LV2-(1-풀이-성공).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59041

### 참고
> 없음

*** 09:55~09:57
### 설계 1분, 총 2분


*/

-- 코드를 입력하세요
SELECT NAME, COUNT(*) AS 'COUNT'
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME ASC;