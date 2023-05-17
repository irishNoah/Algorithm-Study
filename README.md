# Algorithm of BOJ & Programmers

## 폴더 구조(상위 폴더들의 하위 폴더에 대한 설명입니다.)
#### 1) 상위 폴더명 : BAEKJOON(백준 온라인 저지)

|   폴더명   |                      목적                       |     
| :------: | :-----------------------------------------------:|
| 1000~ |                1000번대 이상 문제 풀이                |
| 10000~ |              10000번대 이상 문제 풀이                |
| 단계별 문제 |   백준 단계별 문제 풀이(단계를 하위 폴더로 구분)   | 

* 단계별 문제에서 아직 안 올라온 문제가 있다면 1000~ 또는 10000~ 폴더를 보시고, 만약 이 폴더 내에도 없다면 아직 풀지 않은 문제입니다.

#### 2) 상위 폴더명 : Programmers(프로그래머스)

|   폴더명   |                      목적                       |     
| :------: | :-----------------------------------------------:|
| LV1 |                프로그래머스 LV1 관련 문제 풀이          |
| LV2 |                프로그래머스 LV2 관련 문제 풀이          |

#### 3)상위 폴더명 : 복잡도
- 하위 폴더 X
- 시간 및 공간 복잡도에 대한 개념 사진 첨부
- (출처 : 이것이 코딩 테스트다{저자 : 나동빈 / 출판사 : 한빛미디어})

## 알고리즘 관련 링크
- 알고리즘에 관해 자체 제작 또는 참고한 블로그에 대한 링크입니다.
- 직접 제작한 블로그 포스팅 링크가 있다면 <자체 블로그> 칸에 "Y"로 표기되어 있습니다.
- 직접 제작한 블로그 포스팅 링크가 없다면 <자체 블로그> 칸에 "N"로 표기되어 있습니다.
- <자체 블로그 여부> 칸이 "N"인 경우 제가 아닌 다른 사람이 작성한 블로그의 URL이 첨부되어 있음을 알립니다.

| 순번 |   제목     |    자체 블로그   |    작성일     |     비고     |
|:----------:|:----------:|:----------:|:------:|:------|
| 001 |[그리디 or 탐욕 (개념)](https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%83%90%EC%9A%95%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-greedy-algorithm/)| N | - | * 탐욕 알고리즘 문제 해결 방법<br/>1. 선택 절차: 현재 상태에서의 최적의 해답 선택<br/>2. 적절성 검사: 선택된 해가 문제의 조건을 만족하는지 검사<br/>3. 해답 검사(Solution Check): 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 과정을 반복 |
| 002 | [다이나믹 프로그래밍](https://doing7.tistory.com/75)| N | - | * DP 특징<br/>1. 재귀의 단점(메모리 낭비)을 보완할 수 있는 방식이라 할 수 있다.<br/>2. 일반적으로 구하고자 하는 값을 얻기 위해 이전에 구했던 값들을 활용한다.<br/>- 단, 이전에 구했던 값은 리스트에 저장해서 메모리 및 시간 낭비를 방지한다.<br/>3.점화식(예:피보나치)을 통해 구하고자 하는 값을 구할 수 있다.<br/>4.DP 방식에는 크게 상향식과 하향식이 있다.<br/>- 하향식 방식보다 상향식 방식이 시스템 측면에서 더 좋다.<br/>5. 문제 중에서 최종적으로 구한 값에 대해서 어떠한 큰 수로 나눈 것을 출력하라는 형식의 멘트가 나올 경우, 이 문제는 DP와 관련된 문제일 가능성이 매우 높다. |
| 003 | [재귀의 단점 및 메모이제이션](https://mong9data.tistory.com/22)| N | - | - |
| - | [해시(기초 & 메서드)](https://yunaaaas.tistory.com/46)| N | - | - |
| - | [해시(상세 기술)](https://yunaaaas.tistory.com/46)| N | - | - |
| - | [정렬(선택 & 삽입 & 버블)](https://yunaaaas.tistory.com/46)| N | - | - 선택, 삽입, 버블 정렬은 알고리즘 간단</br>- 효율성은 떨어짐 |
| - | [힙(기초 버전)](https://hocheon.tistory.com/70)| N | - | - 힙의 시간 복잡도 : O(log n)</br>- 리스트 > 힙 변환 시간 복잡도 : O(n) |
| - | [힙(심화 버전)](https://littlefoxdiary.tistory.com/3)| N | - | - |

## 파이썬 자료형 & 메소드 설명 블로그 포스팅
- 파이썬 자료형 및 메소드에 관해 자체 제작 또는 참고한 블로그에 대한 링크입니다.
- 직접 제작한 블로그 포스팅 링크가 있다면 <자체 블로그> 칸에 "Y"로 표기되어 있습니다.
- 알고리즘에 대해 직접 제작한 블로그 포스팅 링크가 없다면 <자체 블로그> 칸에 "N"로 표기되어 있습니다.
- <자체 블로그 여부> 칸이 "N"인 경우 제가 아닌 다른 사람이 작성한 블로그의 URL이 첨부되어 있음을 알립니다.

|   제목    |  자체 블로그  |  작성일   | 비고 | 
| :------: | :-----------------------------------------------:|:------:|:------:|
| [내장 함수](https://wikidocs.net/32)| N | - | abs, all, any, chr, dir, divmod, enumerate, eval,</br> filter, hex, id, input, int, isinstance, len, list,</br>map, max, min, oct, open, dor, pow, range,</br>round, sorted, str, sum, tuple, type, zip |
| [사전(Dictionary)](https://blog.naver.com/park_ckddud/222641153654)| Y | 220207 |  -  |
| [문자열 및 리스트 슬라이싱](https://blog.naver.com/park_ckddud/222645906588) | Y | 220212 |  -  |
| [Counter 클래스](https://blog.naver.com/park_ckddud/222647054180) | Y | 220214 |  -  |
| [숫자로 구성된 문자열 정렬](https://blog.naver.com/park_ckddud/222647086826) | Y | 220214 | sort()와 sort(key = int)의 차이 |
| [집합 자료형 set](https://blog.naver.com/park_ckddud/222650949006) | Y | 220218 | 합/차/교집합 |
| [zip()](https://www.daleseo.com/python-zip/) | N | - | - |
| [람다(lamda)](https://wikidocs.net/64) | N | - | - |
| [2진수 변환 다양한 풀이](https://minnit-develop.tistory.com/17) | N | - | - |
| [문자열에서 특정 문자를 제거하는 5가지 다른 방법](https://ichi.pro/ko/paisseon-eseo-munjayeol-eseo-teugjeong-munjaleul-jegeohaneun-5gaji-daleun-bangbeob-194478292048569) | N | - | - |
| [약수 구하기(시간복잡도 줄여보기)](https://minnit-develop.tistory.com/16) | N | - | - |
| [이중 for문 빠져나가기](https://redmuffler.tistory.com/446) | N | - | - |

## 백준 온라인 저지(BOJ) 문제 블로그 포시틍
- 예전에 푼 문제들은 블로그 포스팅이 안되어 있으며 22년 03월 31일 이후에 푼 문제들로만 블로그 포스팅이 된 점을 말씀드립니다.
- 포스팅 날짜는 실제 문제를 푼 날짜보다 며칠 늦을 수 있습니다.

|   문제 번호    |   제목    |    문제 출처   | 문제 난이도 | 포스팅 날짜 | 사용 언어 |
| :------: |:----------:|:------:|:------:|:------:|:------:|
| [4153](https://velog.io/@irish/BOJ-%EC%A7%81%EA%B0%81%EC%82%BC%EA%B0%81%ED%98%95Python) | 직각삼각형 | BOJ | B3 | 220413 | Python |

## Programmers 문제 블로그 포스팅
- 예전에 푼 문제들은 블로그 포스팅이 안되어 있으며 22년 02월 07일 이후에 푼 문제들로만 블로그 포스팅이 된 점을 말씀드립니다.
- 포스팅 날짜는 실제 문제를 푼 날짜보다 며칠 늦을 수 있습니다.
- 220307일까지는 네이버로 블로그를 제작하였으며, 이후에는 Velog를 통해 제작했음을 알려드립니다.

|   제목     |    문제 출처   | 포스팅 날짜 | 알고리즘 종류 | 사용 언어 |
| :------: |:-----------------------------------------------:|:------:|:------:|:------:|
| [오픈채팅방](https://blog.naver.com/park_ckddud/222641221456)| programmers | 220207 | 분류 없음 | Python |
| [완주하지 못한 선수](https://blog.naver.com/park_ckddud/222641632113)| programmers | 220208 | 해시 | Python |
| [전화번호 목록](https://blog.naver.com/park_ckddud/222645660482)| programmers | 220212 | 해시 | Python |
| [K번째 수](https://blog.naver.com/park_ckddud/222649612140)| programmers | 220216 | 정렬 | Python |
| [가장 큰 수](https://blog.naver.com/park_ckddud/222649623505)| programmers | 220216 | 정렬 | Python |
| [더 맵게](https://blog.naver.com/park_ckddud/222656448767)| programmers | 220224 | 힙 | Python |
| [최댓값과 최솟값](https://blog.naver.com/park_ckddud/222657468434)| programmers | 220225 | 연습문제 | Python |
| [피보나치 수](https://blog.naver.com/park_ckddud/222657475479)| programmers | 220225 | 연습문제 | Python |
| [위장](https://blog.naver.com/park_ckddud/222666507590)| programmers | 220307 | 연습문제 | Python |
| [내적](https://velog.io/@irish/Programmers-%EB%82%B4%EC%A0%81Python)| programmers | 220319 | 연습문제 및 기타 | Python |
| [문자열을 정수로 바꾸기](https://velog.io/@irish/Programmers-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84-%EC%A0%95%EC%88%98%EB%A1%9C-%EB%B0%94%EA%BE%B8%EA%B8%B0Python)| programmers | 220319 | 연습문제 및 기타 | Python |
| [정수 제곱근 판별](https://velog.io/@irish/Programmers-%EC%A0%95%EC%88%98-%EC%A0%9C%EA%B3%B1%EA%B7%BC-%ED%8C%90%EB%B3%84Python)| programmers | 220321 | 연습문제 및 기타 | Python |
| [제일 작은 수 제거하기](https://velog.io/@irish/Programmers-%EC%A0%9C%EC%9D%BC-%EC%9E%91%EC%9D%80-%EC%88%98-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0Python)| programmers | 220321 | 연습문제 | Python |
| [약수의 개수와 덧셈](https://velog.io/@irish/Programmers-%EC%95%BD%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98%EC%99%80-%EB%8D%A7%EC%85%88Python)| programmers | 220321 | 연습문제 | Python |
| [이상한 문자 만들기](https://velog.io/@irish/Programmers-%EC%9D%B4%EC%83%81%ED%95%9C-%EB%AC%B8%EC%9E%90-%EB%A7%8C%EB%93%A4%EA%B8%B0Python)| programmers | 220321 | 연습문제 | Python |
| [정수 내림차순으로 배치하기](https://velog.io/@irish/Programmers-%EC%9D%B4%EC%83%81%ED%95%9C-%EB%AC%B8%EC%9E%90-%EB%A7%8C%EB%93%A4%EA%B8%B0Python-c5bezy8g)| programmers | 220321 | 연습문제 | Python |
| [짝수와 홀수](https://velog.io/@irish/Programmers-%EC%A7%9D%EC%88%98%EC%99%80-%ED%99%80%EC%88%98Python)| programmers | 220322 | 연습문제 | Python |
| [나머지가 1이 되는 수 찾기](https://velog.io/@irish/Programmers-%EB%82%98%EB%A8%B8%EC%A7%80%EA%B0%80-1%EC%9D%B4-%EB%90%98%EB%8A%94-%EC%88%98-%EC%B0%BE%EA%B8%B0Python)| programmers | 220322 | 연습문제 | Python |
| [부족한 금액 계산하기](https://velog.io/@irish/Programmers-%EB%B6%80%EC%A1%B1%ED%95%9C-%EA%B8%88%EC%95%A1-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0Python)| programmers | 220322 | 연습문제 | Python |
| [소수 만들기](https://velog.io/@irish/Programmers-%EC%86%8C%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0Python)| programmers | 220322 | 연습문제 | Python |
| [[1차] 비밀지도](https://velog.io/@irish/Programmers-1%EC%B0%A8-%EB%B9%84%EB%B0%80%EC%A7%80%EB%8F%84Python)| programmers | 220322 | 연습문제 | Python |
| [숫자 문자열과 영단어](https://velog.io/@irish/Programmers-%EC%88%AB%EC%9E%90-%EB%AC%B8%EC%9E%90%EC%97%B4%EA%B3%BC-%EC%98%81%EB%8B%A8%EC%96%B4Python)| programmers | 220323 | 연습문제 | Python |
| [두 정수 사이의 합](https://velog.io/@irish/Programmers-%EB%91%90-%EC%A0%95%EC%88%98-%EC%82%AC%EC%9D%B4%EC%9D%98-%ED%95%A9Python)| programmers | 220323 | 연습문제 | Python |
| [시저 암호](https://velog.io/@irish/Programmers-%EC%8B%9C%EC%A0%80-%EC%95%94%ED%98%B8Python)| programmers | 220323 | 연습문제 | Python |
| [직사각형 별찍기](https://velog.io/@irish/Programmers-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-%EB%B3%84%EC%B0%8D%EA%B8%B0Python)| programmers | 220323 | 연습문제 | Python |
| [최대공약수와 최대공배수](https://velog.io/@irish/Programmers-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98Python)| programmers | 220323 | 연습문제 | Python |
| [가운데 글자 가져오기](https://velog.io/@irish/Programmers-%EA%B0%80%EC%9A%B4%EB%8D%B0-%EA%B8%80%EC%9E%90-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0Python)| programmers | 220323 | 연습문제 | Python |
| [3진법 뒤집기](https://velog.io/@irish/Programmers-3%EC%A7%84%EB%B2%95-%EB%92%A4%EC%A7%91%EA%B8%B0Java)| programmers | 220324 | 연습문제 | Java |
| [모의고사](https://velog.io/@irish/Programmers-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%ACJava)| programmers | 220324 | 완전탐색 | Java |
| [N개의 최소공배수](https://velog.io/@irish/Programmers-N%EA%B0%9C%EC%9D%98-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98Python)| programmers | 220324 | 연습문제 | Python |
| [행렬의 곱셈](https://velog.io/@irish/Programmers-%ED%96%89%EB%A0%AC%EC%9D%98-%EA%B3%B1%EC%85%88Python)| programmers | 220324 | 연습문제 | Python |
| [소수 찾기](https://velog.io/@irish/Programmers-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0Python)| programmers | 220324 | 완전탐색 | Python |
| [최솟값 만들기](https://velog.io/@irish/Programmers-%EC%B5%9C%EC%86%9F%EA%B0%92-%EB%A7%8C%EB%93%A4%EA%B8%B0Python)| programmers | 220324 | 연습문제 | Python |
| [JadenCase 문자열 만들기](https://velog.io/@irish/Programmers-JadenCase-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python-1izrldva)| programmers | 220325 | 연습문제 | Python |
| [다음 큰 숫자](https://velog.io/@irish/Programmers-%EB%8B%A4%EC%9D%8C-%ED%81%B0-%EC%88%AB%EC%9E%90Python)| programmers | 220325 | 연습문제 | Python |
| [이진 변환 반복하기](https://velog.io/@irish/Programmers-%EC%9D%B4%EC%A7%84-%EB%B3%80%ED%99%98-%EB%B0%98%EB%B3%B5%ED%95%98%EA%B8%B0Python)| programmers | 220413 | 연습문제 | Python |
| [멀쩡한 사각형](https://velog.io/@irish/Programmers-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95Python)| programmers | 220413 | 연습문제 | Python |

## irishNoah의 바람
> 개인적으로 푼 문제를 기록하기 위함도 있지만, 많은 분들이 제가 푼 것을 보시고 도움을 받으셨으면 좋겠습니다.
- 화면 상단의 "watch"와 "star"은 저에게 큰 힘이 됩니다!
