def solution(absolutes, signs):
    answer = sum(absolutes)
   
    for i in range(0, len(signs)):
      if signs[i] == False:
            answer -= 2 * absolutes[i]

    return answer

absolutes = [4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))