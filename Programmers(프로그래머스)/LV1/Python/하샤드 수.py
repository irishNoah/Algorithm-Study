def solution(x):
      answer = True
      a = []

      for i in str(x):
            a.append(i)

      for i in range(0, len(a)) :
            a[i] = int(a[i])
      
      sumA = sum(a)

      if x % sumA != 0 :
            answer = False

      return answer