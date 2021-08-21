# 1157번 / 단어 공부 / B1 
txt = input()
arr = []
arr2 = []

# a~z, A~Z 각각 사이의 범위는 25이며
# a의 아스키코드는 97, A의 아스키코드는 65이다.
for i in range(0, 26) :
    txtCount = txt.count(chr(65+i)) + txt.count(chr(97+i))
    arr.append(txtCount)
    arr2.append(txtCount)

# 입력받은 텍스트 안에 있는 알파벳 개수들을 오름차순 정렬 후 내림차순 정렬
arr.sort()
arr.reverse()

# 내림차순 정렬된 것 중 가장 큰 값과(인덱스 0) 그 다음 값(인덱스 1)이 같으면
# 가장 값이 2개인 것이므로 ?를 출력
if arr[0] == arr[1] :
    print('?')

# 값이 다르다면 가장 큰 값이 한 개만 있다는 의미이므로 해당 알파벳을 찾아 출력
else :
    count = 0
    for i in range(0, 26) :
        if arr2[i] == max(arr2) :
            break
        else :
            count = count + 1

    print(chr(65+count))
    
