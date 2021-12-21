def solution(numbers):
      answer = []

      '''
            처음으로 not in이란 것을 사용해 보았다.
            처음에는 그냥 모든 것을 더해주고 그 이후에 set() 메소드로
            중복을 제거하려고 했으나, 이런 방식으로 했었을 경우
            몇 개의 테스트케이스에서 실패가 떴었다.
            이에 따라 not in을 사용하여 애초에 리스트에 담겨진 동일한 것이 있다면
            담지 않게 해주었다. 
            이렇게 해주었더니 모든 테스트케이서에서 성공을 했다.
      '''
      for i in range(0, len(numbers)) :      
            for j in range(i+1, len(numbers)) :
                  if numbers[i] + numbers[j] not in answer:
                        answer.append(numbers[i] + numbers[j])

      answer.sort()

      return answer