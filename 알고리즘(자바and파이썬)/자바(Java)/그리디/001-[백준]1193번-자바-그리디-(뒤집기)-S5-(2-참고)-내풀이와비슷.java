// [백준]1193번-자바-그리디-(뒤집기)-S5-(2-참고)-내풀이와비슷
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1439

/*
내 풀이와 비슷
*/

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		result(str);
	}

	static void result(String str) {
		int zero = 0, one = 0;
		
		if (str.charAt(0) == '0') zero++;
		else one++;
		
		for(int i = 1; i < str.length(); i++) {
			if(str.charAt(i) != str.charAt(i-1)) {
				if (str.charAt(i) == '0') zero++;
				else one++;
			}
		}
		
		System.out.println(Math.min(zero, one));
		
	}
	
}