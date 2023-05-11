# 코드업 100제 
# 6060번-[기초-비트단위논리연산]비트단위로AND하여출력하기(설명)(py).py

'''

입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)

비트단위(bitwise)연산자는,
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
가 있다.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3       : 00000000 00000000 00000000 00000011
5       : 00000000 00000000 00000000 00000101
3 & 5 : 00000000 00000000 00000000 00000001
이 된다.

비트단위 and 연산은 두 비트열이 주어졌을 때,
둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.

이 연산을 이용하면 어떤 비트열의 특정 부분만 모두 0으로도 만들 수 있는데
192.168.0.31   : 11000000.10101000.00000000.00011111
255.255.255.0 : 11111111.11111111.11111111.00000000

두 개의 ip 주소를 & 연산하면
192.168.0.0 :     110000000.10101000.0000000.00000000 을 계산할 수 있다.

실제로 이 계산은 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해
같은 네트워크에 있는지 아닌지를 판단하는데 사용된다.

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서
마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적으로 사용된다.

*****예시
-

*****입력
2개의 정수가 공백을 두고 입력된다.
-2147483648 ~ +2147483647

*****출력
두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.

*****입력 예시
3 5

*****출력 예시
1

'''
# 풀이법 

a, b = input().split()

print(int(a) & int(b))


'''

***** 참고
& (Binary AND) : bit 단위로 and연산을 합니다.
| (Binary OR) : bit 단위로 or연산을 합니다.
^ (Binary XOR) : bit 단위로 xor연산을 합니다.
~ (Binary NOT) : bit 단위로 not연산을 합니다.(1의 보수)
<< (Binary left Shift) : bit 단위로 왼쪽으로 비트단위 밀기 연산을 합니다.
>> (Binary right Shift) : bit 단위로 오른쪽으로 비트단위 밀기 연산을 합니다.

- 비트 단위로 연산을 수행합니다.
- 0은 거짓으로 1은 참으로 연산하여 결과를 1과 0으로 반환합니다.
- "^(xor)"연산은 두개의 값이 다를 때만 참인 연산입니다.
- " ~(not)" 연산은 1의 보수를 구합니다. 컴퓨터에서는 뺄셈을 2의 보수를 덧셈하여 처리 합니다.
- "<<"는 연산은 왼쪽으로 1비트 밀때마다 두 배씩 늘어납니다.
- ">>" 연산은 오른쪽으로 1비트 밀때마다 1/2씩 줄어듭니다.
- n << m : n * 2의 m승
- n >> m : n / 2의 m승

'''