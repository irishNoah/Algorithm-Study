/*
010-[프로그래머스]-SELECT-복습필요(재구매가-일어난-상품과-회원-리스트-구하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131536

### 참고
> 없음

*** 07:52~08:05
### 설계 3분, 총 17분
>>> GROUP BY를 여러개 할 수 있다는 점을 기억하라!!!
- https://gent.tistory.com/505

*/

-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;