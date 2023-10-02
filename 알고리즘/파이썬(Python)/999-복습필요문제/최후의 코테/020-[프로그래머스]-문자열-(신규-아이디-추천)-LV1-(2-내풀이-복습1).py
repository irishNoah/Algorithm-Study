'''
020-[프로그래머스]-문자열-(신규-아이디-추천)-LV1-(2-내풀이-복습1).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/72410

### 참고
> 없음

13:17 ~ 13:44
### 설계 7분, 총 27분
>>> 주어진 규칙 그대로 진행
1. lower()
2. isdigit 이거나 isalpha 이거나 [빼기/밑줄/마침표]이거나
3. replace("..", ".")
4. 문자열[0]이거나 문자열[-1]이 "."일 경우 슬라이싱 활용
5. len(문자열) = 0 이면 > 문자열 = "a"
6. len(문자열) >= 16
    - 문자열 = 문자열[:15]
    - 만약 문자열[-1]이 '.' 이면?
        - 문자열 = 문자열[:14]
7. len(문자열) <= 2
    - while len(문자열) != 3:
        - 문자열 += 문자열[-1]

'''


def solution(new_id):
    new_id = new_id.lower()
    
    word = ""
    for alp in new_id:
        if alp.isdigit() == True or alp.isalpha() == True:
            word += alp
        elif alp in ["-", "_", "."]:
            word += alp
    
    while ".." in word: # 이 while문을 유심있게 처다보자!
        word = word.replace("..", ".")
        
    if word[0] == ".":
        word = word[1:] if len(word) > 1 else "."
        ### if len(word) > 1 else "."
        ### >>> 길이가 1 이하일 경우 그냥 아무것도 처리 안한 상태로
        ### 이 if문을 행햘 경우 인덱스 에러가 발생한다.
        ### 길이가 1 이하인데, word[0]의 값이 "."일 경우 아래 if문에서 처리하도록 한다.
    if word[-1] == ".":
        word = word[:-1]
    
    if len(word) == 0:
        word = "a"
    
    if len(word) >= 16:
        word = word[:15]
        
        if word[-1] == ".":
            word = word[:14]
    
    if len(word) <= 2:
        while len(word) != 3:
            word += word[-1]
    
    return word