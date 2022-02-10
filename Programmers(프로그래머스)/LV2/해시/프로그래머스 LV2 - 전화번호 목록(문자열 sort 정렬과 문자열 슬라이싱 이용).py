# 프로그래머스 LV2 - 전화번호 목록(문자열 sort 정렬과 문자열 슬라이싱 이용)
# https://programmers.co.kr/learn/courses/30/lessons/42577
# 참고[그냥 sort와 key=int를 이용한 sort] : https://pythonq.com/so/python/1537651

# 정확성 테스트의 케이스 19개 중 19개 성공
# 효율성 테스트의 케이스 4개 중 4개 성공 
# 총점 100.0점


def solution(phone_book):
    answer = True # return할 값 answer

    '''
    문자열 정렬하기
    만약 리스트가 ["0", "10", "3", "4", "100"]으로 구성되어 있을 경우에
    phone_book.sort()를 하면 ["0", "10", "100", "3", "4"]로 정렬되고,
    phone_book.sort(key = int)를 하면 ["0", "3", "4", "10", "100"]이 된다.

    두 개의 차이점은 다음과 같다.

    숫자 형태로 이루어진 문자열 리스트에서
    그냥 sort()를 하게 되면 문자열은 사전 순으로 정렬되면 "10"은 "3"보다 앞에 오게 된다.
    그 이유는 ("1" < "3")이기 때문에 첫 번째 문자열에서 "1" 뒤에 오는 것은 무시되기 때문이다.

    반면 sort(key = int) 형태로 정렬하게 되면 숫자 형태의 문자열 리스트 요소들의 값이
    그냥 숫자의 오름차순식의 정렬로 이루어지게 된다.
    즉, sort(key = int)를 하게 되면 리스트는 ["0", "3", "4", "10", "100"]가 되는 것이다.

    문제에서는 특정 번호가 다른 번호의 일부에 해당되는지 확인하는 것이다.
    그렇기 때문에 숫자 오름차순식의 정렬 이후의 값 비교를 하는 것이 아니라
    그냥 sort()를 한 이후 앞의 요소와 뒤의 요소 즉, 인덱스 i와 인덱스 i+1의 값만 비교해주면 되는 것이다.
    
    그렇기 때문에 이 문제에서는 sort(key = int)가 아닌 sort()로 접근해주어야 한다.
    '''
    phone_book.sort()

    '''
    phone_book.sort()로 문자열 정렬 이후에 앞의 요소와 나머지 모든 요소를 비교하는 것이 아니라
    앞의 요소와 바로 다음 요소만 비교해주면 된다.
    
    그 이유는 앞의 요소와 그 다음 요소만 상대적으로 매우 비슷한 형태의 숫자끼리 정렬되어 있기 때문이다.
    
    그러나 phone_book[i+1] == phone_book[i]의 형태는 문자열 값이 다 동일하냐 비교하는 것이므로,
    phone_book[i+1][0:len(phone_book[i])] == phone_book[i] 형태처럼
    문자열 슬라이싱을 통해 앞 요소의 길이 만큼 다음 요소의 값을 슬라이싱 한 상태에서 앞과 뒤 요소를 비교해주어야 한다.
    '''
    for i in range(0, len(phone_book)-1):

        '''
        앞 요소의 값이 뒤 요소의 앞 부분과 동일하다면 answer은 TRUE가 되고, 이렇게 될 경우 더 이상 비교할 필요 없이
        for문을 break 해주면 된다.
        '''
        if phone_book[i+1][0:len(phone_book[i])] == phone_book[i] :
            answer = False
            break

    return answer

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))