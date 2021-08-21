import sys

N = int(sys.stdin.readline())

H = [int(sys.stdin.readline()) for _ in range(N)]

stack, res = [], 0

for i in range(N) :
    while stack != [] and stack[-1] <= H[i] :
        stack.pop()
    stack.append(H[i])
    res += len(stack)-1

print(res)