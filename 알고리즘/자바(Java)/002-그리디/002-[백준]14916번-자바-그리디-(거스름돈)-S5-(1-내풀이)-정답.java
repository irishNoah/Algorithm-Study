// [백준]14916번-자바-그리디-(거스름돈)-S5-(1-내풀이)-정답.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/14916

/*
전체적인 풀이는 다 맞았는데
coin % 5 == 0가 있는 if문에서 출력해야 하는 것 때문에, 다른 곳에서 출력한 것은 실피해고
이후 이 if문에 넣어서 맞게 됐다..
아니 근데, eclipse에서는 다 잘 되고, 단순히 프린트 문 하나 때문에 틀린 판정이 나는 것은 좀 어이 없다.
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	
    	int coin = sc.nextInt();
    	
    	int cnt = 0;
    	
    	while(true) {
    		if (coin < 0) {
    			System.out.println(-1);
    			break;
    		}
    		
    		if (coin % 5 == 0) {
    			cnt += coin / 5;
    			System.out.println(cnt);
    			break;
    		}
    		else {
    			coin = coin - 2;
    			cnt++;
    		}
    	}
    	
    	//System.out.println(cnt);
    	
    }
}