// 코드업-1092-최대공약수(GCD)와최소공배수(lcm)-재귀활용

/*
 BigInteger 에는 최대공약수를 구하는 gcd 함수가 있다.
 이 함수를 사용하면 아주 쉽게 구할 수 있다.
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

	    Scanner sc = new Scanner(System.in);
	    long a = sc.nextLong(); long b = sc.nextLong(); long c = sc.nextLong();

	    // 세 숫자의 최소공배수 구하기
	    long result = lcm(a, lcm(b, c));
	    System.out.println(result);       // 1800

	  }

	  // 최소 공배수 계산 메서드
	  // 최소공배수는 엄청나게 큰 숫자가 나올 수도 있기에
	  // long형으로 다루어야 합니다.
	  public static long lcm(long a, long b) {
	    int gcd_value = gcd((int)a, (int)b);

	    if (gcd_value == 0) return 0; // 인수가 둘다 0일 때의 에러 처리

	    return Math.abs( (a * b) / gcd_value );
	  }


	  // 최대 공약수 계산 함수; 최소 공배수 계산에 필요함
	  // 최대 공약수는 그리 큰 숫자가 나오지 않기에 int형으로
	  public static int gcd(int a, int b) {
	    while (b != 0) {
	      int temp = a % b;
	      a = b;
	      b = temp;
	    }
	    return Math.abs(a);
	  }
}