// [백준]1475번-자바-구현-(방번호)-S5-(1-내풀이)-정답.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1475

/*
1. 문자열 배열 구하기 > str
2. str을 리스트로 전환 > lst (각 자리수 개수를 frequency()로 파악하려고)

# 새로 배운 점
1. for문에서 파이썬 마냥 바로 Array에 접근해서 출력하기
> 참고 URL : https://mainia.tistory.com/3950

2. Array와 ArrayList의 차이
> 참고 URL : https://gayoung78.tistory.com/61

3. Array와 ArrayList에서 중복 값 개수 세기 
> Collections.frequency() 이용 / Map 이용
> 참고 URL : https://hianna.tistory.com/572

*/

import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	String[] str = br.readLine().split("");
    	List<String> lst = Arrays.asList(str);
    	
    	// 각 수가 lst 안에 몇 개씩 있는지 파악
    	int arr[] = new int[9];
    	
    	arr[0] = Collections.frequency(lst, "0"); // 0의 개수
    	arr[1] = Collections.frequency(lst, "1"); // 1의 개수
    	arr[2] = Collections.frequency(lst, "2"); // 2의 개수
    	arr[3] = Collections.frequency(lst, "3"); // 3의 개수
    	arr[4] = Collections.frequency(lst, "4"); // 4의 개수
    	arr[5] = Collections.frequency(lst, "5"); // 5의 개수
    	arr[6] = Collections.frequency(lst, "7"); // 7의 개수
    	arr[7] = Collections.frequency(lst, "8"); // 8의 개수
    	arr[8] = Collections.frequency(lst, "6") + Collections.frequency(lst, "9"); // 6과 9의 개수
    	
    	// 6과 9는 서로 바꾸어 쓸 수 있으므로 다른 수와 다르개 6, 9는 2개 당 1세트라고 보면됨
    	// arr[8]이 짝수면 세트는 이 값의 절반값
    	// 홀수면 절반값 + 1
    	if (arr[8] % 2 == 0) {
    		arr[8] = arr[8] / 2;
    	}
    	else {
    		arr[8] = (arr[8] / 2) + 1;
    	}
    	
    	Arrays.sort(arr);
    	System.out.println(arr[arr.length-1]);
    	
    
    }

}