# 코드업 100제 
# 6014번-[기초-입출력]-실수1개입력받아3번출력하기(py).py

'''
실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

예시
...
print(f)  #f에 저장되어있는 값을 출력하고 줄을 바꾼다.
print(f)
print(f)
와 같은 방법으로 3번 줄을 바꿔 출력할 수 있다.

입력 예시
0.1

출력 예시
0.1
0.1
0.1
'''

val1 = float(input())
print(val1); print(val1); print(val1)

'''
print(f)
print(f)
print(f)

처럼 작성해서 출력을 할 수 있었으나
코드 라인 낭비 문제를 방지하기 위해 세미 콜론(;)을 호라용해서 풀었음
'''