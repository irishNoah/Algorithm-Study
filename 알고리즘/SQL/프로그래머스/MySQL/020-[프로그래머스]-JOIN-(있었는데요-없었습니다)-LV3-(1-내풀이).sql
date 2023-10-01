/*
020-[프로그래머스]-JOIN-(있었는데요-없었습니다)-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/59043

### 참고
> 없음

*** 20:26~20:43
### 설계 4분, 총 19분
> 조회
- I.ANIMAL_ID, I.NAME
> 조인
- INNER JOIN 
- ON I.ANIMAL_ID = O.ANIMAL_ID
> WHERE
- I.DATETIME > O.DATETIME
> 정렬
- I.DATETIME ASC

 
*/

-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME ASC;