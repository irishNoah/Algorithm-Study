import java.util.Scanner;

class Solution {
    public int[] solution(long num) {
     
		String s = Long.toString(num);
        int len = s.length();
		int arr[] = new int[len];
		for(int i = 0; i <len; i++) {
			arr[i] = (int)(num%10);
			num /= 10;
            }
        return arr;
    }
}