/*
026-[프로그래머스]-GROUPBY-복습필요(조건에-맞는-사용자와-총-거래금액-조회하기)-LV3-(1-내풀이-참고).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/164668

### 참고
> https://devwarriorjungi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-164668-MySQL-Level3-%EC%A1%B0%EA%B1%B4%EC%97%90-%EB%A7%9E%EB%8A%94-%EC%82%AC%EC%9A%A9%EC%9E%90%EC%99%80-%EC%B4%9D-%EA%B1%B0%EB%9E%98%EA%B8%88%EC%95%A1-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0

*** 09:38~09:48
### 설계 5분, 총 10분
> 조회
- U.아이디 / U.닉네임 / SUM(B.PRICE)
> 조인(INNER JOIN)
- USED_GOODS_BOARD B / USED_GOODS_USER U
- ON B.WRITER_ID = U.USER_ID
> 조건
- B.STATUS = 'DONE'
> 정렬
- 3 ASC

*/

-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS 'TOTAL_SALES'
FROM USED_GOODS_BOARD B INNER JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY U.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY 3 ASC;