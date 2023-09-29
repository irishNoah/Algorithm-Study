// [프로그래머스]-자바-브루트포스-(숫자의-표현)-LV2-(1-내풀이-성공)-완전탐색.java
// https://github.com/irishNoah/Algorithm-Study
// https://school.programmers.co.kr/learn/courses/30/lessons/12924

/*
# 완전탐색
>>> n은 10000 이하 자연수이므로 O(N^2까지 가능)


1. int num = 1; int answer = 0;
2. while을 돌며 num이 n보다 클 때까지 수행
    - int val = num;
    - int sum = 0;
    - while (true)
        - sum += val
        - 만약 sum이 n보다 작으면 
            - val += 1
            - 계속 진행
        - 만약 sum이 n과 같으면
            - answer은 1 증가
            - break
        - 만약 sum이 n보다 커지면
            - break
    - num += 1
3. asnwer 반환

*/

class Solution {
    public int solution(int n) {
        int answer = 0;
        int num = 1;
        
        while (num <= n){
            int val = num;
            int sum = 0;
            
            while (true){
                //System.out.println("111");
                sum += val;
                
                if (sum < n){
                    val += 1;
                    continue;
                }
                else if(sum == n){
                    answer += 1;
                    break;
                }
                else{
                    break;
                }
            }
            
            num += 1;
        }
        
        
        
        return answer;
    }
}