/*
038-[프로그래머스]-STRING&DATE-복습필요(카테고리 별 상품 개수 구하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/131529

### 참고
>

*** 11:30 ~ 11:37
### 내 설계 1분, 총 7분

### 복습필요
- SUBSTRING( 문자열, 시작위치, 길이 ) >> 문자열에서 시작 위치부터 길이만큼 출력합니다.
- LEFT( 문자열, 길이 ) >> 문자열에서 왼쪽부터 길이만큼 출력합니다.
- RIGHT( 문자열, 길이 ) >> 문자열에서 오른쪽부터 길이만큼 출력합니다.

**************************************************
SELECT SUBSTRING(NAME, 2, 4) // NAME의 2번째글자부터 4글자 출력
     , SUBSTRING(NAME, 1, 4) // NAME의 1번째글자부터 4글자 출력
     , LEFT(MAIL, 7) // MAIL을 왼쪽부터 7글자 출력
     , RIGHT(MAIL, 5) // MAIL을 오른쪽부터 5글자 출력
  FROM TABLE
**************************************************

*/

-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;