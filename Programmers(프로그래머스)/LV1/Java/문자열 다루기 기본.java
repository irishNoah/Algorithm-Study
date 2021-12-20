class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        char checkS;
        
    if(s.length() == 4 || s.length() == 6) {
         for(int i = 0; i < s.length(); i++) {
		    checkS = s.charAt(i);
			    if(checkS >= '0' && checkS <= '9') {
                //
			    }
			    else {
				    answer = false;
			    }
		  }
             return answer;
        }
        
        else{
            answer = false;
            return answer;   
        }
    }
}