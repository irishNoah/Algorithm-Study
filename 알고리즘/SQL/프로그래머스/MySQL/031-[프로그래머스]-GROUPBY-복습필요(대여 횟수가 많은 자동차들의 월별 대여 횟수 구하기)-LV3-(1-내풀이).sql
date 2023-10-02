/*
031-[프로그래머스]-GROUPBY-복습필요(대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기)-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/151139

### 참고
>

*** 22:42~23:11
### 내 설계 12분, 총 30분
> 검색
- (월별) / (자동차ID별) / 월별 기록
> WHERE
- 연도(시작일) = 2022
- 월(시작일) BETWEEN 8~10
- 월별 기록 != 0
> 그룹핑
    - 월별, 자동차ID별
    > HAVING
        - 개수(자동차ID) >= 5
> 정렬
- 1 ASC, 2 DESC

>>>> 내 풀이는 틀린 풀이!
- 실제 정답 풀이는 밑에 예제 2개를 보면서 분석하자!
*/


-- 풀이 1
# CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 
# 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력
SELECT MONTH(H.START_DATE) AS MONTH, H.CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
WHERE H.CAR_ID IN (SELECT HH.CAR_ID 
                  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HH
                  WHERE DATE_FORMAT(HH.START_DATE, '%Y-%m') BETWEEN "2022-08" AND "2022-10"
                  GROUP BY HH.CAR_ID
                  HAVING COUNT(*) >= 5)
    AND DATE_FORMAT(H.START_DATE, '%Y-%m') BETWEEN "2022-08" AND "2022-10"

GROUP BY MONTH, H.CAR_ID
HAVING COUNT(*) != 0 
ORDER BY MONTH ASC, CAR_ID DESC


-- 풀이2
/* 한국어가 제일 어렵다
 1. 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차ID들을 테이블 a로 출력
 1.1 "총 대여 횟수가 5회 이상인 자동차들" -> 자동차ID만 그룹화 하여 대여횟수 카운팅 1차
 1.2 "대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지" -> 날짜 필터링 1차

 2. 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 월별, 자동차 ID 별 총 대여 횟수 출력
 2-2. "총 대여 횟수가 5회 이상인 자동차들에 대해서" -> a번 테이블의 자동차 ID로 필터링 
 2-3. "월별, 자동차 ID 별 총 대여 횟수 출력" -> 월별 그룹화 && 자동차ID 그룹화 하여 대여횟수 카운팅 2차
 2-4. "해당 기간 동안의" -> 날짜 필터링 2차, a 테이블에서 넘겨받은 정보는 자동차 ID 뿐이므로 그걸로만 HISTORY테이블에서 필터링시 08~10월이 아닌 경우도 남아있기 때문에 날짜 필터링을 다시 해줘야 한다.
 2-5. ** 서브쿼리로 나눠 처리해야하는 이유: (자동차ID)로 그룹화, (월별 그룹화 and 자동차ID) 그룹화의 결과값이 다르기 때문에 한 번에 처리가 불가하다.

*/
with a as(
    SELECT CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where date_format(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
    group by CAR_ID
    having count(*) >= 5
)

SELECT date_format(START_DATE, '%m') as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where (date_format(START_DATE, '%Y-%m') between '2022-08' and '2022-10') 
    and CAR_ID in (select * from a)
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc