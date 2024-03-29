# 코드업 100제 
# 6018번-[기초-입출력]-시간입력받아그대로출력하기(설명)(py).py

'''
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

예시
a, b = input().split(':')
print(a, b, sep=':')
와 같은 방법으로 가능하다.

입력
시(hour) 분(minute)이 콜론(':')으로 구분되어 한 줄로 입력된다.

출력
입력받은 시간 형식과 똑같이 "시:분" 형태로 출력한다.

입력 예시
3:16

출력 예시
3:16

'''

hour, minute = input().split(':')
print(hour, minute, sep=":")

'''
참고

input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
sep 는 분류기호(seperator)를 의미한다.

* 리뷰
split()은 기본적으로 공백을 구분한다. 
하지만, 다른 문자(기호)를 중점으로 구분하고 싶다면 split("문자")와 같이 사용해야 한다.

이와 같은 원리로 print(a, b)와 같은 형식은 한 줄 안에서 공백을 두고 a와 b를 출력한다.
하지만, 공백이 아닌 다른 문자로 대체하고 싶다면, sep를 활용해해야 한다!
'''