# https://github.com/irishNoah/Algorithm-Study
# 2581번 / 소수 / S5
# https://www.acmicpc.net/problem/2581

# 자연수 m, n 입력
m = int(input())
n = int(input())

# m 이하의 수 중 소수와, n 이하의 수 중 소수를 각각 구하기 위해
# m_setting, n_setting 선언
# 추후에 구한 소수 리스트를 set로 변경 후 뺄 때 문제에서 M 이상 N 이하의 자연수 중
# 소수인 것을 고르라 했으므로 m_setting 초기화 시 (m-2)를 해준 것임
m_setting = [False,False] + [True]*(m-2)
n_setting = [False,False] + [True]*(n-1)

# m과 n의 소수 리스트 m_primes, n_primes
m_primes = []
n_primes = []

# 에라토스테네스의 체를 활용하여 m,n의 소수 목록을 구함
for i in range(2,m):
  if m_setting[i]:
    m_primes.append(i)
    for j in range(2*i, m, i):
        m_setting[j] = False

for i in range(2,n+1):
  if n_setting[i]:
    n_primes.append(i)
    for j in range(2*i, n+1, i):
        n_setting[j] = False

# m과 n의 set 선언
set_m = set(m_primes)
set_n = set(n_primes)

# 차집합을 minus_set_nTOm에 구함
minus_set_nTOm = set_n-set_m

# minus_set_nTOm의 길이가 0이라면 -1 출력
if len(minus_set_nTOm) == 0:
    print(-1)

# minus_set_nTOm의 총합 값과 최소값을 차례대로 출력
else:
    print(sum(minus_set_nTOm))
    print(min(minus_set_nTOm))