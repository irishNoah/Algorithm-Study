# 프로그래머스 LV2 - 멀쩡한 사각형
# 분류 - Summer/Winter Coding(2019)
# https://programmers.co.kr/learn/courses/30/lessons/62048
# 정확성 테스트의 케이스 18개 중 18개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(w,h):
    gcd_value = 0

    # 유클리드 호제법을 이용하여 w, h의 최대공약수 구하기
    for i in range(min(w, h), 0, -1):
        if w % i == 0 and h % i == 0:
            gcd_value = i
            break

    '''
    한 직각삼각형 안에 멀쩡한 정사각형 갯수를 구하는 공식은 다음과 같다.
    참고 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=orbis1020&logNo=220674508134
    (대각선에 의해 잘려진 사각형의 개수) : (가로) + (세로) - (가로 세로의 최대공약수)

    즉, 이것을 w = 8, h = 12를 대입했을 때 (가로 세로의 최대공약수) = 4이므로
    (대각선에 의해 잘려진 사각형의 개수) = 8 + 12 - 4 = 16이다.

    문제에서 8, 12가 주어졌을 때 답이 80이었다.
    이것을 통해 알 수 있는 것이 있는데, 그것은 다음과 같다.
    멀쩡한 사각형 = 가로 * 세로 - (대각선에 의해 잘려진 사각형의 개수)

    이것을 바로 answer에 적용한다.
    '''
    answer = (w * h) - (w + h - gcd_value)

    return answer

w = 12
h = 8
print(solution(w,h)) # 결과 예 : 80