def solution(arr, divisor):
     # 리스트 answer 선언
    answer = []

    count = 0

    # arr의 각 리스트 값 중 divisor로 나눠지는 요소에 대해서만 answer 값에 넣음
    for i in range(0, arr.__len__()) :
      if(arr[i] % divisor == 0) :
          answer.append(arr[i])
          count = count + 1

    if count == 0 :
      answer.append(-1)
    else :
      # answer의 요소에 대해 오름차순 정렬
      answer.sort()
    
    # answer 반환
    return answer