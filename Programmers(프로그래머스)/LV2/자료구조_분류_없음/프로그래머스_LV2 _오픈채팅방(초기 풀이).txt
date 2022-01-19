# 프로그래머스_LV2 _오픈채팅방(초기 풀이)
# 총 32개의 테스트 중 24개 통과 8개 실패
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = [] # 결과값을 답을 리스트 answer

    command = [] # 명령어(Enter, Leave, Change)를 담을 리스트 command
    user_id = [] # 유저 아이디를 담을 리스트 user_id
    user_nickname = [] # 닉네임을 담을 리스트 user_nickname
    find_index = []  # 동일한 아이디가 존재하는 리스트 요소의 인덱스 값 정보를 담는 리스트 find_index

    for i in range(0, len(record)):
        # record 안의 각 요소에 대해 공백을 기준으로 구분한 문자열을 담을 리스트 split_command
        # 참고로 구분하였을 때 split_command[0]은 명령어, split_command[1]은 유저 아이디, split_command[2]는 닉네임에 해당
        split_command = record[i].split()

        command.append(split_command[0]) # 명령어(Enter, Leave, Change)를 command에 삽입


        # 만약 첫 번째 문자열이 "Enter"라면
        if split_command[0] == "Enter": 
            # command.append(split_command[0]) # "Enter"를 command에 삽입

            if split_command[1] in user_id: # 만약 해당 아이디가 기존 user_id에 있었던 아이디라면
                # 동일한 아이디가 존재하는 리스트 요소의 인덱스 값 정보를 담는 리스트 find_index
                # find_index를 통해 동일한 아이디를 갖고 있는 user_id 값의 인덱스를 파악한다.
                find_index = [j for j in range(len(user_id)) if user_id[j] == split_command[1]] 

                # 찾은 인덱스 값에 맞게 기존 user_nickname의 값을 새로운 닉네임으로 변경
                for k in find_index:
                    user_nickname[k] = split_command[2]

            # 만약 해당 아이디가 기존 user_id에 있었던 아이디라면 위 if문 실행 후 아래 2Line 실행
            # 만약 해당 아이디가 기존 user_id에 없었던 아이디라면 바로 아래 2Line 실행
            user_id.append(split_command[1]) # 해당 아이디를 user_id에 삽입
            user_nickname.append(split_command[2]) # 해당 닉네임을 user_nickname에 삽입

        # 만약 첫 번째 문자열이 "Change"라면    
        elif split_command[0] == "Change": 
            # command.append(split_command[0]) # "Change"를 command에 삽입

            # find_index를 통해 동일한 아이디를 갖고 있는 user_id 값의 인덱스를 파악한다.
            find_index = [j for j in range(len(user_id)) if user_id[j] == split_command[1]] 

            # 찾은 인덱스 값에 맞게 기존 user_nickname의 값을 변경된 닉네임으로 변경
            for k in find_index:
                user_nickname[k] = split_command[2]

            user_id.append(split_command[1]) # 마지막에 명령된 해당 아이디를 user_id에 삽입
            user_nickname.append(split_command[2]) # 마지막에 명령된 해당 닉네임을 user_nickname에 삽입

        # 만약 첫 번째 문자열이 "Leave"라면    
        elif split_command[0] == "Leave": 
            # command.append(split_command[0]) # "Leave"를 command에 삽입
            
            # Leave 명령어는 닉네임까지 입력을 하지는 않기 때문에 닉네임을 파악하기 위해서
            # 입력된 해당 아이디와 동일한 값을 가지고 있는 리스트의 인덱스를 
            # index() 메소드를 활용하여 find_lastID_index에 담음
            find_lastID_index = user_id.index(split_command[1])

            # find_lastID_index를 이용하여 닉네임을 찾음
            find_nickname = user_nickname[find_lastID_index]

            user_id.append(split_command[1]) # 해당 아이디를 user_id에 삽입
            user_nickname.append(find_nickname) # find_nickname을 통해 찾은 닉네임을 user_nickname에 삽입

    # answer 값 정의해주기
    for i in range(0, len(command)):
        if command[i] == "Enter":
            answer.append(user_nickname[i]+"님이 들어왔습니다.")

        elif command[i] == "Leave":
            answer.append(user_nickname[i]+"님이 나갔습니다.")

        else:
            continue


    return answer # 최종 결과값 예 : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# ----------------------------------------------------------------------------------------------------------------
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))