# https://github.com/irishNoah/Algorithm-Study
# 10610번 / 30 / S5
# https://www.acmicpc.net/problem/10610

'''
최종 풀이

이 문제는 해당 수가 3의 배수임을 알기 위한 공식을 알아야 풀 수 있다.
해당 수의 모든 자릿수의 합이 3의 배수가 되면 된다.
또한, 3이 아닌 30의 배수이므로 숫자 내에 0이 없다면 -1을 출력해야 한다.

1. 받은 숫자 내에 0이 없다면 -1 출력
2. 숫자들의 합이 3으로 나누어 떨어지지 않는다면 -1 출력
3. 걸러진 수를 내림차순으로 정렬 (언제 해도 상관은 없음)
'''

n = input()
n = sorted(n, reverse=True)
sum = 0
if '0' not in n:	# 우선은 input의 디폴트인 string으로 받았기에 '0' 문자로 적음
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0 :	# 3의 배수 체크
        print(-1)
    else :
        print(''.join(n))