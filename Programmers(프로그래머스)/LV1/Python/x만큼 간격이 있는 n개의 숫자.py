def solution(x, n):
      # 리스트 변수명 answer 선언
    answer = []
    # a라는 변수에 x 값을 초기화
    a = x
    # 리스트 0번째 값으로 a 대입 즉, answer(0) = a
    answer.append(a)

    for i in  range(1,n) : # answer(0)번째 요소는 이미 있으므로 i는 1부터 시작
      # 첫 번째 요소부터 n-1까지 요소까지 answer 리스트에 a+x 값 대입
      answer.append(a+x)
      # 2,4,6,8,10 이든 4,8,12든 간에
      # a = a+x 을 통해 다음 answer.append(a+x)에서 a가 제대로 증가하도록 선언
      a = a+x 


    # answer 반환
    return answer