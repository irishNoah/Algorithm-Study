// [백준]1874번-자바-스택-(스택수열)-S2-(2-참고)-챗지피티.java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1874

/*
이해 참고 URL
> https://loosie.tistory.com/349  
 */
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] sequence = new int[n];
        for (int i = 0; i < n; i++) {
            sequence[i] = scanner.nextInt();
        }

        Stack<Integer> stack = new Stack<>();
        StringBuilder operations = new StringBuilder();

        int current = 1;
        for (int i = 0; i < n; i++) {
            while (current <= sequence[i]) {
                stack.push(current);
                operations.append("+\n");
                current++;
            }

            if (stack.peek() == sequence[i]) {
                stack.pop();
                operations.append("-\n");
            } else {
                System.out.println("NO");
                return;
            }
        }

        System.out.println(operations);
    }
}
