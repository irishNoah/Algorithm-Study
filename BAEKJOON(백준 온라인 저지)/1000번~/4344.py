#  테스트 케이스 개수에 대한 변수 C 선언
C = int(input())

for _ in range(C) :
    # list 타입 변수명 nums 선언 후 공백으로
    # 학생 수와 각 학생의 점수에 대해 입력 받음
    nums = list(map(int, input().split()))

    # 평균에 관한 변수 avg 선언
    # nums[0]은 학생 수
    # nums[1:]은 첫번째 학생부터 마지막 학생까지
    avg = sum(nums[1:])/nums[0]

    # 평균을 넘은 학생 수를 세는 변수 cnt 선언
    cnt = 0
    for score in nums[1:]:
        if score > avg :
            cnt += 1
    
    # 평균을 넘은 학생 수를 비율로 표현하는 변수 rate 선언
    rate = cnt/nums[0]*100
    
    # f스트링을 통해 소수점 3째짜리까지 구한 후 그 뒤에 %를 붙여 출력 
    print(f'{rate:.3f}%')

