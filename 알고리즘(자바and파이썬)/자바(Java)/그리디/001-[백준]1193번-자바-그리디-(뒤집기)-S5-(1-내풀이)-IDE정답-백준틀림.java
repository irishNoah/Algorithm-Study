// [백준]1193번-그리디-(뒤집기)-S5-(1-내풀이)-IDE정답-백준틀림
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1439

/*
IDE에서는 잘 맞았는데, 왜 틀렸는지 모르겠다.
시간 초과, 메모리 초과도 아닌데 틀린 것을 보니 그냥 백준의 의도와는 다르게 푼 것 같다. 
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

	    Scanner sc = new Scanner(System.in);

	    String s = sc.next();
	    char arr[] = s.toCharArray();
	    
	    
	    int countA = 0; int countB = 0;
	    
	    // 뒤집기 최소 횟수 구하기
	    for (int i = 1; i < s.length(); i++) {
	    	if(arr[i] == arr[i-1]) {
	    		continue;
	    	}
	    	
	    	else {
	    		if(arr[i] == '0') {
	    			countA += 1;
	    		}
	    		else {
	    			countB += 1;
	    		}
	    	}
	    }
	    
	    // 출력
	    if (countA == 0) {
	    	System.out.println(countA);
	    	System.exit(0);
	    }
	    if (countB == 0) {
	    	System.out.println(countB);
	    	System.exit(0);
	    }
	    if (countA > 0 && countB > 0) {
	    	if(countA <= countB) {
		    	System.out.println(countA);
		    }
		    else {
		    	System.out.println(countB);
		    }
	    }
	    
	    sc.close();
	    
	  }

}