# 프로그래머스 LV2 - 오픈채팅방(완료)
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = [] # 결과값을 답을 리스트 answer
    # uid와 닉네임을 각각 키와 값으로 매칭 시킬 dictionary 자료형 dic_uid_nick
    dic_uid_nick = {} 

    for word in record :
        word_split = word.split()

        if len(word_split) == 3:
            dic_uid_nick[word_split[1]] = word_split[2]

    for word in record :
        word_split = word.split()

        if word_split[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." %dic_uid_nick[word_split[1]])
        elif word_split[0] == 'Leave':
            answer.append("%s님이 나갔습니다." %dic_uid_nick[word_split[1]])
   

    return answer # 최종 결과값 예 : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# ----------------------------------------------------------------------------------------------------------------
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))