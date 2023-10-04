/*
006-[프로그래머스]-GROUPBY-복습필요-(진료과별-총-예약-횟수-출력하기)-LV2-(1-참고).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/132202

### 참고
> https://school.programmers.co.kr/questions/50271

*** 22:25~22:38
### 설계 5분, 총 13분

*/

-- 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD)=2022 AND MONTH(APNT_YMD) = 5
-- WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY 2, 1;