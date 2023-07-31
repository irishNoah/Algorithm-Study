# [프로그래머스]-파이썬-중간고사2번-그리디-(티셔츠)-(1-내풀이-성공)-pop활용.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 15분 소요] / 총 풀이 시간[총 40분 소요]
> 데이터의 크기가 5000인 것을 감안하면 시간 복잡도 O(N * log N) 이하로 설계를 해야한다.
> 우선, 사람 상체 크기 리스트인 people과 티셔츠츼 크기인 tshirts를 정렬한다. >>> O(N) 복잡도
    - 단, people은 오름차순으로 tshirts는 내림차순으로 정렬한다.
        - 왜냐? pop() 메소드를 쓸 거거든
> 나머지는 코드를 보며 참고

*** 참고

'''
#===================================================================================

def solution(people, tshirts):
    answer = 0

    people = sorted(people) # 사람 상채는 오름차순 정렬
    tshirts = sorted(tshirts, reverse=True) # 티셔트는 내림차순 정렬

    cnt = 0 # people 리스트 인덱스
    while True:

        # 조건에 부합하든 안하든 어차피, tshirts의 마지막 요소는 pop을 통해서 제거해준다.
        if people[cnt] <= tshirts[-1]: # 부등호 방향 때문에 10분은 보낸 듯 ㅎ..
            answer += 1
            cnt += 1
            tshirts.pop()

        else:
            tshirts.pop()

        # 인덱스 에러를 방지하기 위한 해당 조건 및 종료 조건
        if len(tshirts) == 0 or cnt == len(people):
            break

    return answer

#===================================================================================

# 예제 1
people = [3, 2]
tshirts = [2, 1, 3]
print(solution(people, tshirts)) # 2

# 예제 2
people = [3, 1, 2]
tshirts = [1, 1]
print(solution(people, tshirts)) # 1

# def solution(people, tshirts):
#     answer = 0
#     return answer