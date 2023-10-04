/*
032-[프로그래머스]-STRING&DATE-(자동차 평균 대여 기간 구하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/157342

### 참고
>

*** 10:36 ~ 10:50 
### 내 설계 4분, 총 분
> 메인 쿼리
    - 자동차 ID, 평균 대여 기간(컬럼명: AVERAGE_DURATION)
        - 평균대여기간 >>> ROUND( ((SUM(DATEDIFF(종료일,시작일)+1)) / COUNT(*)), 1)
> 그룹핑 자동차 ID
    - HAVING AVERAGE_DURATION >= 7
> 정렬
    - AVERAGE_DURATION DESC
    - 자동차 ID DESC

*/

-- 코드를 입력하세요
SELECT CAR_ID, ROUND( ((SUM(DATEDIFF(END_DATE,START_DATE)+1)) / COUNT(*)), 1) AS 'AVERAGE_DURATION'
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID                         ###  평균 대여 기간이 7일 이상인 자동차
    HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;