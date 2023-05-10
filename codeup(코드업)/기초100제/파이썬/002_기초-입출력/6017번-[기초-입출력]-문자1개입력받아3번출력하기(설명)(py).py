# 코드업 100제 
# 6017번-[기초-입출력]-문자1개입력받아3번출력하기(설명)(py).py

'''
정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

예시
s = input()
print(s, s, s)  #공백으로 구분해 한 줄로 출력한다.
와 같은 방법으로 3번 출력할 수 있다.

입력 예시
computer science

출력 예시
computer science computer science computer science

'''

val = input()
print(val, val, val)

'''
참고

python 언어에서는 문자/정수/실수/문자열 등 특별한 구분이 없이도 원하는 변수에 저장시켜 출력 할 수 있다.
하지만, 저장된 값을 이용해 계산하거나 서로 붙여 연결시키거나 잘라내는 작업을 한다면?
반드시 저장되어있는 값의 종류(문자/정수/실수/문자열 등)를 구분해 주어야 한다.

'''