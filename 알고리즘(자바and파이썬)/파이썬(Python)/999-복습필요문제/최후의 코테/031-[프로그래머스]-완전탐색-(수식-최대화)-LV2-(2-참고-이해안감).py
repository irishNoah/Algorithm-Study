'''
031-[프로그래머스]-완전탐색-(수식-최대화)-LV2-(2-참고-이해안감).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/67257

### 참고
> https://americanoisice.tistory.com/170

### 설계 분, 총 분
1. 주어진 expression에 대해 for에 idx 기준으로 접근하여
isdigit()을 통해서, 숫자와 수식을 구분한다.
2. 있는 수식을 기준으로 수식 우선순위를 구한다.
3. 수식 우선순위에 따라 계산을 진행하여, result 리스트에 할당한다.
    - 구해진 계산이 음수일 경우에는, abs()를 통해 절댓값으로 변환한 것으로
    result에 할당한다.
4. result의 최댓값을 return한다.

'''

def solution(expression):
    # 연산자가 3개만 있으므로 애초에 모든 경우의 수를 구해 놓는다.
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            print("temp = ", temp)
            temp_list.append(f'({b.join(temp)})')
            print("temp_list = ", temp)
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)