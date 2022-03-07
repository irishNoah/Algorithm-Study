def solution(clothes):
    answer = 0 # 리턴할 값 answer
    cloths = {}
    
    # clothes에 담겨있는 옷들을 한개씩 뽑아와서 종류별로 카운팅을 해준다.
    for name, kind in clothes:
        # 이미 들어와 있는 종류이면 저장된값에서 1을 저장해준다.
        if kind in cloths:
            cloths[kind]+=1
        # 처음 들어오는 종류이면 1로 저장 
        else:
            cloths[kind] = 1
    
    answer = 1
    # 아이템들의 개수를 한개씩 뽑아오기
    for key, value in cloths.items():
        # 각 (아이템의 개수+1)을 해준다. +1을 해주는이유는 해당아이템을 착용하지 않는경우도 포함
        answer *= (value+1)
        
    # 구한 정답에 -1을 해준다. 모든 종류를 안입는 경우는 없으므로 -1을 해주어야한다.
    return answer-1 


clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))