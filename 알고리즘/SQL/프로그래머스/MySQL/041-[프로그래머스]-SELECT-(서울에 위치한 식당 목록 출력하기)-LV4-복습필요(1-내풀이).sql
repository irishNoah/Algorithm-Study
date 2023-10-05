/*
041-[프로그래머스]-SELECT-(서울에 위치한 식당 목록 출력하기)-LV4-복습필요(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131118

### 참고
>

*** 23:56 ~ :
### 내 설계 7분, 총 분


*/

-- 코드를 입력하세요
SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO I
INNER JOIN REST_REVIEW R ON I.REST_ID = R.REST_ID
WHERE I.ADDRESS LIKE '서울%'
GROUP BY 1
ORDER BY SCORE DESC, I.FAVORITES DESC