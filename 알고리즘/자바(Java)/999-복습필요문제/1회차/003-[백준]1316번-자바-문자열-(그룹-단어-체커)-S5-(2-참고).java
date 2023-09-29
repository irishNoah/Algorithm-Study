// [백준]1316번-자바-문자열-(그룹-단어-체커)-S5-(2-참고).java
// https://github.com/irishNoah/Algorithm-Study
// https://www.acmicpc.net/problem/1316

/*
charAt()으로 접근한 것은 좋았는데... 아쉽다
 */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = n;  //그룹 단어의 개수
        for (int i = 0; i < n; i++) {
            boolean[] arr = new boolean[26];  //이미 나타난 문자 확인용
            String s = br.readLine();
            arr[(int)s.charAt(0) - 97] = true;  //우선 첫 단어 확인
            for (int j = 1; j < s.length(); j++) {
                char c = s.charAt(j);
                //이전 문자와 같으면 continue
                if (c == s.charAt(j-1)) continue;

                //이전 문자와 다르고 이미 나타난 문자면 그룹 단어가 아니므로 count - 1
                if (arr[(int)c - 97]) {
                    count--;
                    break;
                }
                arr[(int)c - 97] = true;  //나타난 단어라고 확인
            }
        }
        System.out.println(count);
    }
}
