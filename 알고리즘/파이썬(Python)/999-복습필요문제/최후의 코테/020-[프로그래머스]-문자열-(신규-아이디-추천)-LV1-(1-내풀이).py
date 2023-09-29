'''
020-[프로그래머스]-문자열-(신규-아이디-추천)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/81301

### 설계 5분, 총 37분
> rstrip(), lstrip() 보다는 그냥 슬라이싱 활용하자
> 3, 4단계를 집중적으로 복습하자

'''

def solution(s):
    s = s.lower() # 1단계
    
    # 2단계
    word = ""
    for idx in range(len(s)):
        if s[idx].isalpha() == True or s[idx].isdigit() == True or s[idx] in ['-', '_', '.']:
            word += s[idx]
    
    # 3단계
    while ".." in word:
        word = word.replace("..", ".")
    
    # 4단계
    if word[0] == ".":
        word = word[1:] if len(word) > 1 else "."
    if word[-1] == ".":
        word = word[:-1]
    
    # 5단계
    if len(word) == 0:
        word = "a"
    
    # 6단계:
    if len(word) > 15:
        word = word[:15] ### 인덱스 범위 잘 확인하자!
    
        if word[-1] == ".":
            word = word[:-1]
    
    # 7단계
    if len(word) < 3:
        cmp = word[-1]
        while len(word) != 3:
            word += cmp
    
    return word