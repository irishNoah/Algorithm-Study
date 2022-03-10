# 프로그래머스 LV1 - 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

# 정확성 테스트의 케이스 16개 중 16개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(s):
    '''
    @ 문자열 s를 공백으로 구분하여 리스트 type 형식으로 변환하기

    * 주의할 점은 s = s.split()이 아닌 s = s.split(" ")로 해야 한다는 점이다.
    그 이유는 다음과 같다.
    
    문제 입출력 예에서 s는 "try hello world"이다. 이 때에는 s = s.split()로 해도
    원하는 값 자체는 얻을 수 있다.

    그러나 만약 s가 s = "try   hello          world"와 같이 space(띄어쓰기)가
    하나로 단어가 구분된 것이 아니라 여러개의 space로 띄어져 있다면
    문제가 발생한다.

    만약, 위 s에서 s = s.split()을 한다면
    해당 solution 함수의 리턴은 "TrY HeLlO WoRlD"이지만,
    s = s.split(" ")을 한다면
    해당 solution 함수의 리턴은 "TrY   HeLlO          WoRlD"이다.

    즉, 각 단어 사이에 space가 얼마나 있느냐에 따라 그 개수에 맞게 결과 값에도
    단어 사이에 동일한 space가 있어야 한다는 점이다.

    이 점을 명심해야 한다.

    '''
    s = s.split(" ")
    print(s)

    # 리스트 s의 인덱스를 지정하기 위한 check_bit
    check_bit = 0

    for word in s:
        """
        word는 문자열이므로 각 word마다 리스트로 접근하여 슬라이싱을 해주고
        이를 split_word에 대입한다.
        예를 들어 word가 "hello"일 경우 list(word)를 split_word에 대입하면
        split_word = ['h', 'e', 'l', 'l', 'o']가 된다.
        """
        split_word = list(word)


        for i in range(0, len(split_word)):
            if split_word[i] == " ":
                continue

            # i를 2로 나눈 나머지가 0이면 대문자로 치환
            if i % 2 == 0 :            
                split_word[i] = word[i].upper()

            # i를 2로 나눈 나머지가 1이면 소문자로 치환
            else:
                split_word[i] = word[i].lower()


        word = "".join(split_word)

        s[check_bit] = word
        check_bit += 1

    # 리스트 형태의 s를 문자열 형태로 변환
    s = " ".join(s)

    return s

s = "try   hello          world"
print(solution(s))