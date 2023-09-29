'''
009-[프로그래머스]-완전탐색-(카펫)-LV2-(1-내풀이).py

### 설계 11분, 총 15분
'''

def solution(brown, yellow):
    answer = []
    
    hap = brown + yellow # 전체 카펫의 크기(넓이)
    
    # 가로 길이가 세로보다 크거나 같으므로 내림차순으로 약수 탐색
    for idx in range(yellow, 0, -1):
        if yellow % idx == 0:
            garo = idx
            sero = (yellow // idx)
            
            if hap == (garo+2) * (sero+2):
                return [garo+2, sero+2]
    
    return answer