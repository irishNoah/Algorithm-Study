/*
006-[프로그래머스]-GROUPBY-복습완료-(진료과별-총-예약-횟수-출력하기)-LV2-(2-내풀이).sql
### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/133024

07:53 ~ 7:58
### 설계 4분, 총 5분
> 검색
    - 진료과코드 / 5월예약건수
> WHERE
    - 2022년 5월
> 그룹핑
    - 진료과코드
> 정렬
    - 2 ASC, 1 ASC

*/

-- 코드를 입력하세요
SELECT MCDP_CD, COUNT(*)
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, "%Y-%m") = '2022-05'
GROUP BY MCDP_CD
ORDER BY 2 ASC, 1 ASC;