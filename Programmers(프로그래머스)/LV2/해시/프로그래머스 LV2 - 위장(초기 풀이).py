def solution(clothes):
    answer = 0 # 리턴값에 해당되는 변수 answer

    # 2차원 리스트를 딕셔너리로 전환
    dic_clothes = dict(clothes)

    # 옷이 총 몇 개 있는지 파악하기 위한 변수 cnt_clothes
    cnt_all_clothes = list(dic_clothes.values())

    # 옷의 종류가 중복되지 않은 것끼리는 섞어서 입을 수 있으므로
    # 옷의 종류마다 몇 개씩 있는지 파악하기 위한 변수 cnt_same_category_clothes
    cnt_same_category_clothes = list(set(cnt_all_clothes))

    # 동일한 옷의 종류가 몇 개씩 파악하기 위한 리스트 list__mix_clothes
    list__mix_clothes = []

    # 동일한 옷의 종류가 몇 개씩 파악하기 위해 for 문을 돌림
    for i in range(0, len(cnt_same_category_clothes)):
        value = cnt_same_category_clothes[i]
        cnt_value = cnt_all_clothes.count(value)
        list__mix_clothes.append(cnt_value)

    if len(list__mix_clothes) <= 1:
        answer = len(cnt_all_clothes)

    else :
        answer = len(cnt_all_clothes) + eval('*'.join([str(n) for n in list__mix_clothes]))

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	
print(solution(clothes))