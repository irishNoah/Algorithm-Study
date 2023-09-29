# [프로그래머스]-파이썬-그리디-(큰수만들기)-LV2-(2-참고).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

'''
참고 URL
https://suminig.tistory.com/14

# 설명
> 스택을 활용해서 풀어야 함
> 스택이 비어있지 않고, 스택의 마지막 아이템이 현재 들어오는 숫자보다 작다면 계속해서 지워주는 방법
> 다만, number = 10000, k = 2 같은 경우는 계속해서 들어오는 0이 stack[-1]와 같기 때문에 아무 숫자도 지워지지 않는다.
- 따라서 마지막에 k가 0이 아닐 경우를 대비해 stack에서 k만큼 자른 값을 반환하면 된다.
'''
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    return "".join(stack) if k == 0 else "".join(stack[:-k])

number = input()
k = int(input())

print(solution(number, k))
