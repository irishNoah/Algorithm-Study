# 1712번 / 손익분기점 / B4 
# https://www.acmicpc.net/problem/1712

# A는 고정비용, B는 가변 비용, C는 한 대의 노트북 가격
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

# 만약 B가 C보다 크거나 같으면 손익분기점이 존재할 수 없으므로 -1을 출력
if B >= C :
    print("-1")

# B가 C보다 작을 경우 아래 코드를 수행
else :
    print(int(A/(C-B)) + 1)
