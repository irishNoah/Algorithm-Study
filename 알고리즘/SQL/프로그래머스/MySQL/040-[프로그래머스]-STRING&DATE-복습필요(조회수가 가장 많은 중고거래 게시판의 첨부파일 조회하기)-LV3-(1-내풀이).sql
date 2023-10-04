/*
040-[프로그래머스]-STRING&DATE-복습필요(조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기)-LV3-(1-내풀이).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/164671

### 참고
>

*** 11:56 ~ :
### 내 설계 분, 총 분


*/

-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', UGF.BOARD_ID, '/', UGF.FILE_ID, UGF.FILE_NAME, UGF.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD AS UGB, USED_GOODS_FILE AS UGF
WHERE UGB.BOARD_ID = UGF.BOARD_ID AND
    UGB.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_PATH DESC