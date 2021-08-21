# 백준 5598 - 카이사르 암호(구현, 문자열)
# 문제
# 가이우스 율리우스 카이사르(Gaius Julius Caesar)는 
# 고대 로마 군인이자 정치가였습니다. 
# 카이사르는 비밀스럽게 편지를 쓸 때, 'A'를 'D로', 'B'를 'E'로, 'C'를 'F'로... 
# 이런 식으로 알파벳 문자를 3개씩 건너뛰어 적었다고 합니다.

# 26개의 대문자 알파벳으로 이루어진 단어를 카이사르 암호 형식으로 
# 3문자를 옮겨 겹치지 않게 나열하여 얻은 카이사르 단어가 있습니다. 
# 이 카이사르 단어를 원래 단어로 돌려놓는 프로그램을 작성하세요.

# 각 문자별로 변환 전과 변환 후를 나타낸 건 아래와 같습니다.
#       변환전    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
#       변환후    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

# 예를 들어서, 이 방법대로 단어 'JOI'를 카이사르 단어 형식으로 변환한다면 
# 'MRL'을 얻을 수 있고, 앞의 예와 같은 방법으로 얻은 
# 카이사르 단어 'FURDWLD'를 원래 단어로 고치면 'CROATIA'가 됩니다.

# 입력
# 입력은 한 줄로 이루어져 있으며, 
# 그 한 줄엔 대문자 알파벳으로 구성된 단어가 1개 있습니다.

# 입력받는 단어는 최대 1000자 이하입니다.

# 출력
# 출력은 입력받은 카이사르 단어를 원래 단어로 고친 걸 출력하시면 됩니다.

# 예제 입력 1 
# MRL

# 예제 출력 1 
# JOI

# ----------------------------------------------------------------

# 변수 word에 문자열로 입력받기
word = input()
# print(type(word))

# 문자열 word에 대해 한 글자씩 나눠 저장하기 위해
# wordCvt라는 변수에 word를 list로 Casting 시키기
wordCvt = list(word)

# 아래를 통해 a-z까지 26개, A-Z까지 26개가 있다는 것을 확인할 수 있다.
# 또한 97~122, 65~90은 각각 소문자 및 대문자 알파벳에 대한 아스키 코드이다.
# 즉, ord 함수를 사용하면 그 알파벳 또는 문자 또는 숫자 등에 대한
# 아스키 코드를 확인할 수 있다.
# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90

# 애초에 카이사르 암호는 A를 D로, B를 E로 표기 했다.
# 즉 원래 문자로 돌리기 위해서는 D를 A로, E를 B로 변환하기 위해서는
# 입력받은 알파벳에 대해서 3을 빼야한다.

# 3칸씩 뺏을 때에 대한 정보를 담아두는 list인 listendElement 선언
listendElement = []

# 입력된 문자열의 각 알파벳에 대해 3씩 증가 시키기
for i in range(0, len(wordCvt)) :
    # 각 알파벳에 대해 증가 시켜야 하므로
    # 각 알파벳을 대입할 변수 changeWordCvtElement 선언 
    # 그 후 for문마다 wordCvt[i] 대입
    changeWordCvtElement = wordCvt[i]

    # ordValue라는 변수에 각 알파벳에 대한 아스키코드 값에 3을 더해준 값을
    # 저장하여 나중에 3이 밀렸을 때(즉, 더했을 때) 바뀐 알파벳 아스키코드에 대해
    # 또 알파벳으로 변환하기 위하여 일단 ordValue 선언
    # for문을 돌 때마다 알파벳이 변경되므로 0으로 초기화해야 한다.
    ordValue = 0

    # changeWordCvtElement가 대문자 A-Z 중에 있다면 이에 대해 3씩 증가시킴
    if ord(changeWordCvtElement) >= 65 and ord(changeWordCvtElement) <= 90 :
        # A, B, C는 3을 뺏을 때 90 미만이므로 26을 우선 더해야 한다. 그 다음 3을 뺀다.
        # 그래야 올바른 알파벳이 나온다.
        # 즉, A -> X, B -> Y, C -> Z로 변환해주기 위함
        if ord(changeWordCvtElement) >= 65 and ord(changeWordCvtElement) <= 67 :
            ordValue = ord(changeWordCvtElement) + 26 - 3
        
        # A, B, C를 제외한 나머지 알파벳은 그냥 3만 빼주면 된다.
        else : 
            ordValue = ord(changeWordCvtElement) - 3

        # 이제 아스키코드를 문자열로 변환해주자
        # 이를 위해 변경된 알파벳이라는 변수 endElement를 선언하고
        # 이에 chr(ord(changeWordCvtElement)) 대입한다.
        endElement = chr(ordValue)
        
        # 이것을 listendElement에 append한다.
        listendElement.append(endElement)


# 이제, 변환된 알파벳 리스트 listendElement를 하나의 문자열로 변환시키기 위해
# unionListEndElemnt 변수를 선언하고 lsitendElement를 합친 것을 대입하자.
# lsitendElement를 합치기 위해서는 join 함수를 사용하면 되며
# 사용 방법은 아래와 같다.
# "".join(map(str, 리스트 변수명))
unionListEndElemnt = "".join(map(str, listendElement))

# 합쳐진 문자열 출력하기
print(unionListEndElemnt)

