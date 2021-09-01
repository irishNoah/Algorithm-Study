# 2908 / 상수 / B5
# https://www.acmicpc.net/problem/2908

# 두 수를 공백으로 구분하여 입력받기
a, b = map(int, input().split())

# 두 수 각각 각 자리를 분할하기 위한 리스트인 listA, listB 선언
listA = []
listB = []

# 각 수를 str 타입으로 넣어주어 각 자리를 분해한 다음 각 리스트에 넣어줌
# 예 : 수 = 123을 아래 for문에 넣어주면 리스트 ['1','2','3']이 됨
for i in str(a) :
    listA.append(i)

for i in str(b) :
    listB.append(i)

# 상수가 수학을 못해 수를 거꾸로 본다고 문제에 나와 있으므로
# 가운데 수는 그대로 두고, 앞 자리와 뒷 자리 숫자만 바꾸어준다.
x = listA[0]
listA[0] = listA[2]
listA[2] = x

y = listB[0]
listB[0] = listB[2]
listB[2] = y

# 리스트 자체는 하나의 수(또는 단어)가 아니므로
# 리스트를 join() 함수를 통해 합쳐준다. 
cvtA = ''.join(listA)
cvtB = ''.join(listB)

# 윗 변수는 타입이 int가 아닌 str이므로 정수 타입인 int로 변환해준다.
cvtA = int(cvtA)
cvtB = int(cvtB)

# 첫 번째 수가 두 번째 수보다 크거나 같으면 첫 번째 수 출력
if cvtA >= cvtB :
    print(cvtA)

# 위의 경우가 아니라면 두 번째 수 출력
else :
    print(cvtB)