# 프로그래머스 LV1 - K번째 수(초기풀이)
# https://programmers.co.kr/learn/courses/30/lessons/42748

# 정확성 테스트의 케이스 7개 중 7개 성공
# 효율성 테스트는 없었음
# 총점 100.0점

def solution(array, commands):
    answer = [] # 리턴해야 할 리스트 answer

    for i in range (0, len(commands)):
        # commands 안에 있는 하나의 요소(예: [2, 5, 3])를 
        # for문을 이용하여 하나씩 분리하기 위한 리스트 range_list
        range_list = commands[i]

        # array 리스트를 commands 안에 있는 하나의 요소에 있는 i, j에 맞게 슬라이싱 하고자
        # 슬라이싱 한 이후의 리스트 slice_list
        slice_list = array[range_list[0]-1:range_list[1]]

        slice_list.sort() # 슬라이싱 한 리스트 오름차순 정렬

        # slice_list 안에서 k에 해당되는 수를 찾아 answer에 append
        answer.append(slice_list[range_list[2]-1])

        # print(slice_list)

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))