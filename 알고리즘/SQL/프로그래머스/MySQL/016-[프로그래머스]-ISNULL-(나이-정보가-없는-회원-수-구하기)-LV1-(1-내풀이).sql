/*
016-[프로그래머스]-ISNULL-(나이-정보가-없는-회원-수-구하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131528

### 참고
> 없음

*** 09:23~09:24
### 설계 1분, 총 1분

*/


-- 코드를 입력하세요
SELECT COUNT(*)
FROM USER_INFO
WHERE AGE IS NULL;