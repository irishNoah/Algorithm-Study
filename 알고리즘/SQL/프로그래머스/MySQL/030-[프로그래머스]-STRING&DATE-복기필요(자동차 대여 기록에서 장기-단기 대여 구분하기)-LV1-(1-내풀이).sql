/*
030-[프로그래머스]-STRING&DATE-복기필요(자동차 대여 기록에서 장기/단기 대여 구분하기)-LV1-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/151138

### 참고
> https://devwarriorjungi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-157343-MySQL-Level1-%EC%9E%90%EB%8F%99%EC%B0%A8-%EB%8C%80%EC%97%AC-%EA%B8%B0%EB%A1%9D%EC%97%90%EC%84%9C-%EC%9E%A5%EA%B8%B0%EB%8B%A8%EA%B8%B0-%EB%8C%80%EC%97%AC-%EA%B5%AC%EB%B6%84%ED%95%98%EA%B8%B0

*** 20:27~20:47
### 내 설계 3분, 총 20분
> 조회
- 히스토리 id(대여기록 아이디), 자동차ID, 시작일, 종료일
- CASE
    - 종료일 - 시작일 < 30 -> '단기대여'
    - 나머지 -> '장기대여'
    - END AS RENT_TYPE
- WHERE >>> 2022년 5월
- 정렬
    - 히스토리 ID DESC

### 복기
>>> DATEDIFF(END_DATE, START_DATE)+1
- 1을 더해줘야 하는 이유
    - 시작일과 종료일이 같다고 하더라도 대여일은 1일로 계산되어야 하기 때문
        - 이것 때문에 시간 잡아먹음 ㅎㅎㅎ
*/

-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, "%Y-%m-%d") AS 'START_DATE',  DATE_FORMAT(END_DATE, "%Y-%m-%d") AS 'END_DATE', 
    CASE 
        WHEN DATEDIFF(END_DATE, START_DATE)+1 < 30 THEN '단기 대여' ### 복기 필요 구간
        ELSE '장기 대여'
    END AS 'RENT_TYPE'
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) = 9
ORDER BY HISTORY_ID DESC;