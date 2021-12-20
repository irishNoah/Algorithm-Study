def solution(arr1, arr2):
      answer = []

      for i in range(len(arr1)) :
            arr_sum = []
            for j in range(len(arr1[0])) :
                  arr_sum.append(arr1[i][j] + arr2[i][j])
            
            answer.append(arr_sum)

      return answer

arr1 = [[1,2],[2,3]]	
arr2 = [[3,4],[5,6]]

print(solution(arr1, arr2))