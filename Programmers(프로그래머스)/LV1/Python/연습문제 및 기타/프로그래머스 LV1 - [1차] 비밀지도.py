# 프로그래머스 LV1 - [1차] 비밀지도
# 분류 - 기타(2018 KAKAO BLIND RECURITMENT)
# https://programmers.co.kr/learn/courses/30/lessons/17681

# 정확성 테스트의 케이스 8개 중 8개 성공
# 효율성 테스트는 없었음
# 총점 100.0

def solution(n, arr1, arr2):
    answer = []

    # zip()을 이용해 arr1과 arr2의 요소들을 차례대로 접근
    for pair_1, pair_2 in zip(arr1, arr2):
        '''
        pair_1과 pair_2를 bin 메소드를 통해 비트 접근자 OR를 해주고
        OR를 해주면 예를 들어 "0b******" 등의 형식으로 표현되는데,
        앞의 "0b"는 필요 없으므로 문자열 슬라이싱을 활용하여
        이를 or_bin_value 변수에 할당함
        '''
        or_bin_value = str(bin(pair_1|pair_2)[2:])

        '''
        rjust 메소드를 활용하여 or_bin_value를 오른쪽 정렬하여
        n 보다 길이기 작으면 앞에는 0으로 채워줌
        '''
        or_bin_value = or_bin_value.rjust(n, '0')

        '''
        replace 메소드를 활용하여 0은 스페이스(" ")로
        1은 "#"으로 대체
        '''
        or_bin_value = or_bin_value.replace("0"," ")
        or_bin_value = or_bin_value.replace("1","#")

        # 최종적으로 얻은 or_bin_value 값을 answer에 append 해줌 
        answer.append(or_bin_value)

    return answer

n = 6	
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2)) # 출력 예 : ["#####","# # #", "### #", "# ##", "#####"]