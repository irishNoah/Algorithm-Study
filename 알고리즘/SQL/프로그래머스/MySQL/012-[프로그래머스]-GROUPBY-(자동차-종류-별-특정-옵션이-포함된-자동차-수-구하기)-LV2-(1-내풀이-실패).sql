/*
012-[프로그래머스]-GROUPBY-(자동차-종류-별-특정-옵션이-포함된-자동차-수-구하기)-LV2-(1-내풀이-실패).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/151137

### 참고
> 없음

*** 09:09~09:17
### 설계 1분, 총 8분
> https://medium.com/learn-from-data/having%EC%9D%98-%EB%B9%84%EB%B0%80-7ebf56834436
- Unknown column 'OPTIONS' in 'having clause'

*/

-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(*) AS 'CARS'
FROM CAR_RENTAL_COMPANY_CAR
GROUP BY CAR_TYPE
HAVING OPTIONS = '통풍시트' OR OPTIONS = '열선시트' OR OPTIONS = '가죽시트';
