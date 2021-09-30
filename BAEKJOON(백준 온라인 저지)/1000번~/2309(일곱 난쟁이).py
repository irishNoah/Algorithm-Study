# 2309 / 일곱 난쟁이 / B2
# https://www.acmicpc.net/problem/2309

# 일단 문제의 난쟁이 수가 9명이므로 N을 9로 초기화
N = 9

# 9명의 난쟁이의 각각의 키에 대한 정보를 담기 위한 리스트 tall 선언
tall = []

# N, 즉 9번 만큼 난쟁이의 키를 입력 받고, 그 값을 tall에 append()
for _ in range(0,N) :
       human_tall = int(input())
       tall.append(human_tall)

# 일단 리스트 tall을 내림차순 정렬
tall.sort(reverse=True)

# 난쟁이 7명의 키의 합이 100이 나와야 하므로 9명의 키를 모두 합산한 것에서 100을 빼면
# 초과되는 나머지 키가 나온다. 예를 들어 9명의 난쟁이 키의 합이 140이면 필요 없는 키가 40이다.
# 따라서 그 필요 없는 키 40에 대해 두 난쟁이의 키의 합산이 이를 충족한다면 그 두 명을 빼면 된다.

# 위 주석의 원리를 이용하여 필요 없는 키, 즉 나머지에 대한 변수 remain을 선언하고
# 9명 난쟁이의 키를 sum()을 통해 합산하고 여기에서 100을 뺀 후, remain에 대입한다.
remain = sum(tall) - 100

# 이중 for문을 활용하여 두 난쟁이의 키가 필요 없는 키에 충족할 시 안에 있는 for 문을
# break하여 탈출시킨다고 하여도, 안에 있는 for만 탈출한 것이지 밖에 있는 for문을 탈출한 것이 아니기 때문에
# 만약 안에 있는 for문이 조건을 충족하여 break를 탈출한다면, 사실상 밖에 있는 for문도 더이상 돌릴 필요성이 없으므로
# 이를 위하여 breakType이라는 변수를 선언하고 True 값을 대입한다.
breakType = True

for i in range(0,N) :
    for j in range(0,N-1):
        # 내림차순 순으로 하여 두 명의 난쟁이의 키 값을 합산한다.
        sum = tall[i] + tall[j]

        # 그 값이 만약 필요 없는 키와 일치하면 아래 if문을 수행한다.
        if remain == sum :
            # tall[i] 값을 tall_one_value라는 변수에 대입
            tall_one_value = tall[i]

            # tall[j] 값을 tall_two_value라는 변수에 대입
            tall_two_value = tall[j]
            
            # tall리스트에서 각각 tall_one_value, tall_two_value 값을 가지고 있는 
            # 리스트 요소를 remove() 메소드를 통해 제거
            tall.remove(tall_one_value)
            tall.remove(tall_two_value)

            # 문제에서 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다. 라는 조건이 있기 때문에
            # 실질적으로 처음 필요 없는 키를 충족하는 것을 제외한 나머지 리스트 요소만 출력하기 때문에
            # 더이상 for문을 돌릴 필요가 없다.

            # 그렇게 때문에 breakType을 False로 하여 안에 있는 for문을 탈출한 후 
            # 밖에 있는 for문 역시 break 시키게 한다.
            breakType = False

            # 이중 for문 중 안에 있는 for문 탈출
            break
        
        # 그 값이 만약 필요 없는 키와 일치하지 않는다면 계속 안쪽 for문을 실행한다.
        else :
            continue

    # 안의 for문에서 조건과 부합하여 breakType가 False가 되었다면, 밖에 있는 for문 역시 break를 시행한다.
    if breakType == False :
        break

# 기존 tall이 내림차순으로 위에서 정렬되었지만, 출력에서는 오름차순으로 출력해주어야 하기 때문에
# 다시 reverse() 메소드를 수행하여 오름차순 정렬을 한다.
tall.reverse()

# 난쟁이 키를 오름차순으로 하나씩 하나씩 출력한다.
for i in range(0, len(tall)) :
    print(tall[i])