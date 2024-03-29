# 코드업 100제 
# 6007번-[기초-출력]-출력하기07(설명)(py).py

'''
문제

윈도우 운영체제의 파일 경로를 출력하는 연습을 해보자.
파일 경로에는 특수문자들이 포함된다.
다음 경로를 출력하시오.

"C:\Download\'hello'.py"
(단, 따옴표도 함께 출력한다.)

 
\도 안전하게 출력하려면 \\를 사용하는 것이 좋다.
'''

print("\"C:\\Download\\'hello'.py\"")

'''
* 001
문자열 출력을 위해 문자열을 쌍따옴표로 묶었을 때
만약, 이 문자열 안에 쌍따옴표를 출력하고자 한다면 이 앞에 역슬래쉬를 사용해야 한다.

* 002
반대로 작은따옴표로 묶었을 때
만약, 이 문자열 안에 작은따옴표를 출력하고자 한다면 이 앞에 역슬래쉬를 사용해야 한다.

* 003
그러나 문자열 안에서 \(역슬래쉬)도 안전하게 출력하고자 한다면
문제에서 암시했던 것처럼 \\로 입력하는 것이 좋다.
\\로 사용하지 않았더니 출력시 \가 출력되지 않는 문제가 발생하기 때문이다.
'''