# 참고 : https://injekim97.tistory.com/455
# 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/42587
# 프로그래머스_LV2_프린터

from collections import deque

def solution(priorities, location):
    answer = 0 # return을 위한 answer
    # index_list는 말 그대로 priorities에 받은 리스트의 인덱스들을 deque로 저장
    # 예 : [2, 1, 3, 2] -> # deque([0, 1, 2, 3])
    index_list = deque([i for i in range(len(priorities))])
    maxinum = max(priorities) # [2, 1, 3, 2] 중 3이 가장 큼

    while True:
        # deque([0, 1, 2, 3])에서 왼쪽부터 하나씩 방출 즉 0, 1, 2, 3 순
        index = index_list.popleft() 

        # 즉 priorities[0], priorities[1], priorities[2], priorities[3] < maxinum이라면
        if priorities[index] < maxinum:
            # [2, 1, 3, 2]에서 2를 pop 했으니, 제일 뒤로 보내주기 위해 append를 사용
            # 즉, [1, 3, 2, 2]가 되는 것임. 이러한 과정을 반복
            index_list.append(index)

        # 예 : priorities[2,1,3,2] -> index_list = deque([0,1,2,3])
        # 즉, priorities[0,1,2,3] 중에 maxinum과 같다면?
        else:
            answer += 1
            priorities[index] = 0 # 같다면 그 값을 0으로 만든 후
            maxinum = max(priorities) # maxinum을 업데이트함 
        
            # 또한, index와 location의 위차가 같다면?
            if index == location:
                return answer



# 대기목록 리스트 priorities
# 각 리스트 요소는 중요도를 나타내며 값이 클수록 중요함
priorities = [2, 1, 3, 2]

# 인쇄를 요청한 문서에 대한 변수 location
# 만약 priorities가 [A, B, C, D]이고 location이 2라면
# 요청 문서는 C에 해당함
location = 2

print(solution(priorities, location))