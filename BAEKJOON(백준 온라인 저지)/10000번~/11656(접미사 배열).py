# 11656 / 접미사 배열 / S4
# https://www.acmicpc.net/problem/11656

# 문자열 value 선언 및 입력
value = input()

# value의 길이를 valueLen이라는 변수에 대입
# 이유 : 바로 및 for문에서 반복 횟수를 구하기 위함
valueLen = len(value)

# 각 접미사에 대한 정보를 담기 위한 list인 valueList 선언
valueList = []

# for문을 통해 입력 받은 문자열에 대한 접미사를 구하여 valueList에 할당
for _ in range(0, valueLen) :
    # valueList에 value를 append() 메소드를 통하여 할당
    valueList.append(value)

    # value[1:]을 통해 문자열에서 맨 앞 요소를 제외한 나머지 문자열을 담을 수 있다.
    # 예 > 기존 value = "abcd"일 경우 value[1:]은 "bcd"가 된다.
    # 따라서 value[1:]의 값을 다시 value 변수에 할당
    value = value[1:]

# 위 for문을 통해 모든 접미사가 구해졌고, 사전순으로 정렬을 해주는 것이 문제에서 요구한 것이므로
# sort() 메소드를 통해 valueList 안에서 사전순으로 정렬을 해준다.
valueList.sort()

# 단순히 print(valueList)로 출력을 하면 문제에서 원하는 출력 형식이 아니기 때문에
# for문을 통해서 각 리스트 요소를 index인 i를 통해 각 요소의 값을 출력한다.
for i in range(0, len(valueList)) :
    print(valueList[i])