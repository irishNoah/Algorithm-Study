/*
027-[프로그래머스]-GROUPBY-복습필요(즐겨찾기가-가장-많은-식당-정보-출력하기)-LV3-(1-내풀이-참고).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131123

### 참고
> https://devwarriorjungi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-131123-MySQL-Level3-%EC%A6%90%EA%B2%A8%EC%B0%BE%EA%B8%B0%EA%B0%80-%EA%B0%80%EC%9E%A5-%EB%A7%8E%EC%9D%80-%EC%8B%9D%EB%8B%B9-%EC%A0%95%EB%B3%B4-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0

*** 10:08~10:18
### 설계 분, 총 분
> 조회
- 음식종류 / 식당 아이디 / 식당 이름 / 즐겨찾기 수
> 그룹핑
- 음식종류
- HAVING MAX(즐겨찾기)
> 정렬
- 음식종류 DESC

*/

-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (    
    SELECT FOOD_TYPE, MAX(FAVORITES) 
    FROM REST_INFO    
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC;