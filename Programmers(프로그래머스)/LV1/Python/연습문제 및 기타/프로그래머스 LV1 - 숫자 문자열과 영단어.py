# 프로그래머스 LV1 - 숫자 문자열과 영단어
# 분류 - 기타(2021 카카오 채용연계형 인턴십)
# https://programmers.co.kr/learn/courses/30/lessons/81301

# 정확성 테스트의 케이스 10개 중 10개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(s):
    # answer에 문자열 s 대입
    answer = s

    # 영단어로 이루어진 숫자(zero~nine)을
    # 숫자로 이루어진 문자열(0~9)로 replace() 메소드를 이용해서 치환
    answer = answer.replace('zero', '0') 
    answer = answer.replace('one', '1') 
    answer = answer.replace('two', '2')
    answer = answer.replace('three', '3')
    answer = answer.replace('four', '4')
    answer = answer.replace('five', '5')
    answer = answer.replace('six', '6')
    answer = answer.replace('seven', '7')
    answer = answer.replace('eight', '8')
    answer = answer.replace('nine', '9')

    # answer도 str 타입이므로 return은 int 타입으로 강제 형 변환하여 돌려줌
    return int(answer)

s = "one4seveneight" 		
print(solution(s)) # 출력 예 : 1478