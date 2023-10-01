/*
015-[프로그래머스]-GROUPBY-(입양-시각-구하기(1))-LV2-(1-풀이-성공).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59412

### 참고
> 없음

*** 09:58~10:02
### 설계 1분, 총 분


*/

-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS 'HOUR', COUNT(*) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME) ASC;