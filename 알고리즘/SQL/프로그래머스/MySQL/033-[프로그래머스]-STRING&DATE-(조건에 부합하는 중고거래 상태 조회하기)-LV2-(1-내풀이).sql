/*
033-[프로그래머스]-STRING&DATE-(조건에 부합하는 중고거래 상태 조회하기)-LV2-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/164672

### 참고
>

*** 10:57 ~ 11:03 
### 내 설계 1분, 총 6분


*/

-- 코드를 입력하세요
SELECT B.BOARD_ID, B.WRITER_ID, B.TITLE, B.PRICE, 
    CASE 
        WHEN B.STATUS = 'SALE' THEN '판매중'
        WHEN B.STATUS = 'RESERVED' THEN '예약중'
        ELSE '거래완료'
    END AS 'STATUS'
FROM USED_GOODS_BOARD B
WHERE DATE_FORMAT(B.CREATED_DATE, "%Y-%m-%d") = '2022-10-05'
ORDER BY B.BOARD_ID DESC;