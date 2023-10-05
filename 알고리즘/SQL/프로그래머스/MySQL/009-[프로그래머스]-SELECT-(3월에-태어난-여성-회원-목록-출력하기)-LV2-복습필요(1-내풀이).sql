/*
009-[프로그래머스]-SELECT-(3월에-태어난-여성-회원-목록-출력하기)-LV2-복습필요(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131120

### 참고
> 없음

*** 07:39~07:47
### 설계 1분, 총 8분
>>> 문제 좀 꼼꼼히 잘 읽자
>>> DATE 지정 형식
- DATE_FORMAT(DATE 타입의 COL명, '%Y-%m-%d')

*/


-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 AND TLNO IS NOT NULL
AND GENDER = 'W'
ORDER BY MEMBER_ID;