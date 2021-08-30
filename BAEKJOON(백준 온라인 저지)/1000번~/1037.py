# 1037 / 약수 / S5
# https://www.acmicpc.net/problem/1037

# 약수의 개수 입력
n = int(input())

# 진짜 약수를 리스트 형식 x에 입력
x = list(map(int, input().split()))

# 만약 약수의 개수와 x의 길이가 일치하지 않으면 안되므로
# 일치하지 않을 시 다음 if문 수행
if n != len(x) :
    print("리스트의 길이가 입력된 길이보다 길거나 짧습니다.")

# x 오름차순 정렬
x.sort()
# x의 1번째 원소와 마지막 원소를 곱한 값을 대입한 check 변수 선언
check = x[0] * x[-1]

# check의 약수의 개수를 파악하기 위한 리스트 checkList 선언
checkList = []

# 2부터 check전까지 차례대로 나머지가 0인 숫자에 대해 checkList에
# append 해주기
for i in range(2, check) :
    if check % i == 0 :
        checkList.append(i)

# 만약 x와 checkList 값이 동일하다면 옳은 것이므로
# 그냥 check를 출력해준다.
if x == checkList :
    print(check)