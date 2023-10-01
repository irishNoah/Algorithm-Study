/*
019-[프로그래머스]-JOIN-(없어진-기록-찾기)-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59042

### 참고

*** 20:15~20:23
### 설계 6분, 총 8분
>>> 합집합 상태에서 B-A인 상황
    - RIGHT OUTER JOIN
> 검색 : 동물ID, 동물 이름
> 조인
    - INS 테이블 RIGHT OUTER JOIN OUT 테이블 ON INS의 동물 ID = OUTS의 동물 ID
> WHERE
    - INS 테이블의 ID가 IS NULL
> 정렬
 - 동물 ID ASC
 
*/

-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I RIGHT OUTER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID ASC;