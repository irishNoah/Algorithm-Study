/*
023-[프로그래머스]-SELECT-복습필요(조건에-부합하는-중고거래-댓글-조회하기)-LV1-(1-내풀이-정답).sql

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/164673

### 참고
> 없음

*** 08:50~09:10
### 설계 분, 총 분
> 검색(게시글 B / 댓글 R)
- 게시글 제목 / 게시글 아이디 / 댓글 ID / 댓글 작성자 ID / 댓글 컨텐츠 / 댓글 작성일
- 댓글 작성일의 DATE_FORMAT >>> "%Y-%m-%%d"
> 조인(INNER JOIN)
- 게시글의 BOARD_ID = 댓글 BOARD_ID
> 조건
- 댓글의 연도 = 2022 AND 월 = 10
> 정렬
- 6 ASC, 1 ASC

### 복기
> 2022년 10월에 작성된 것이 게시글인가 댓글인가???


*/

-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, "%Y-%m-%d") AS 'CREATED_DATE'
FROM USED_GOODS_BOARD B INNER JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
WHERE YEAR(B.CREATED_DATE) = 2022 AND MONTH(B.CREATED_DATE) = 10
ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;