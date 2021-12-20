class Solution {
    public String solution(String[] seoul) {
       //count를 통해 Kim서방이 어디 있는지 확인할 것임.
		int count = 0;
        
        for(int i = 0; i < seoul.length; i++) {
			if(seoul[i].equals("Kim")) {
				count = i;
			}
		}
        
        String answer = "김서방은 " + count + "에 있다";
        return answer;
    }
}