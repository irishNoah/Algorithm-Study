/*
021-[프로그래머스]-JOIN-(오랜-기간-보호한-동물(1))-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59044

### 참고
> 없음

*** 20:49~20:53
### 설계 3분, 총 4분
> 조회 : I.NAME, I.DATETIME
> 조인
- LEFT OUTER JOIN
- ON : 두 테이블의 ANIMAL_ID
> WHERE
- 아웃츠 테이블.아이디 IS NULL
> 정렬
- I.DATETIME ASC
> LIMIT 3

*/

-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT OUTER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME ASC
LIMIT 3;