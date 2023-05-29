// [백준]1193번-자바-그리디-(뒤집기)-S5-(3-참고)-토큰활용.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1439

/*
# 참고 문제 소스 URL
https://nahwasa.com/entry/%EB%B0%B1%EC%A4%80-1439-%EC%9E%90%EB%B0%94-%EB%92%A4%EC%A7%91%EA%B8%B0-BOJ-1439-JAVA

# 토큰나이저에 대한 설명(split() 메소드와의 비교 포함)
https://jhnyang.tistory.com/entry/JAVA-StringTokenizer-%ED%81%B4%EB%9E%98%EC%8A%A4%EB%A1%9C-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%84%EB%A6%AC%ED%95%98%EA%B8%B0-split-%EB%B9%84%EA%B5%90
*/

/*
StringTokenizer > 문자열을 토큰화한다.

java.util.StringTokenizer 임포트 필요

##### StringTokenizer 생성방법
1. StringTokenizer st = new StringTokenizer(문자열); >>> 띄어쓰기 기준으로 문자열 분리
2. StringTokenizer st = new StringTokenizer(문자열, 구분자); >>> 구분자 기준으로 문자열 분리
3. StringTokenizer st = new StringTokenizer(문자열, 구분자, true 또는 false); 
>>> 구분자를 기준으로 문자열을 분리할 때, 구분자도 토큰으로 넣을지(true) / 구분자는 분리된 문자열 토큰에 포함 안시킬지(false)

##### StringTokenizer 대표 메서드
1. hasMoreTokens [리턴값 : boolean] > 역할 : 남아있는 토큰이 있으면 true를 리턴, 더 이상 토큰이 없으면 false 리컨
2. nextToken() [리턴값 : String] > 역할 : 객체에서 다음 토큰을 반환
3. countTokens() [리턴값: int] > 역할 : 총 토큰의 개수를 리턴

##### StringTokenizer와 split의 차이
- 둘 다 문자열 파싱하는데 사용할 수 있다.
- StringTokenizer는 java.util에 포함되어 있는 클래스 / split은 String 클래스에 속해있는 메소드이다.
- StringTokenizer는 문자 또는 문자열로 문자열을 구분한다면 / split은 정규표현식으로 구분한다.
- StringTokenizer는 빈 문자열을 토큰으로 인식하지 않지만  / split은 빈 문자열을 토큰으로 인식한다.
- StringTokenizer는 겨로가값이 문자열이라면 split은 결과 값이 문자열 배열이다.
따라서 StringTokenizer를 이용할 경우, 전체 토큰을 보고 싶다면 반복문을 이용해서 하나하나 뽑을 수밖에 없다.
- 배열을 담아 반환하는 split는 데이터를 바로바로 잘라서 반환해주는 StringTokenizer보다 성능이 약간 뒤쳐질 수 있다.
 */

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringTokenizer st1 = new StringTokenizer(s, "0");
        StringTokenizer st0 = new StringTokenizer(s, "1");
        System.out.println(Math.min(st1.countTokens(), st0.countTokens()));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}