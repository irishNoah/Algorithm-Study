# https://github.com/irishNoah/Algorithm-Study
# 10610번 / 30 / S5
# https://www.acmicpc.net/problem/10610

'''
초기 풀이

VScode 상에서는 실행이 잘 됐으나, 백준 제출 시 시간 초과 판정을 받았다.
'''

num = int(input())

num_list = list(str(num))
num_list = sorted(num_list, reverse=True)

cnt = 0
cnt_ck = len(num_list)

max_value = -1

while 1:
  if cnt >= cnt_ck:
    break

  elif num_list[0] == '0':
    if cnt >= cnt_ck:
      break

    else:
      cnt += 1
      num_list.append(num_list.pop(0))

      continue

  value_cnt = int(''.join(num_list))

  if value_cnt % 30 == 0:
    max_value = value_cnt
    break

  num_list.append(num_list.pop(0))

  cnt += 1

print(max_value)