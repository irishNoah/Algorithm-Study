'''
018-[프로그래머스]-문자열-(숫자-문자열과-영단어)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/81301

### 설계 9분, 총 25분


'''

def solution(s):
    answer = 0
    
    num = {
        "zero" : "0", "one" : "1", "two" : "2",
         "three" : "3", "four" : "4", "five" : "5",
         "six" : "6", "seven" : "7", "eight" : "8",
         "nine" : "9",
    }
    
    word = ""
    test = []
    for i in range(len(s)):
        if s[i].isdigit() == True: # 숫자라면
            test.append(s[i])
        
        else: # 숫자가 아니라면
            word += s[i]
            
            if word in num.keys():
                test.append(num[word])
                word = ""

    return int("".join(test))