class Solution {
    public boolean solution(int x) {
        
          int sum = 0;
	      int total = x;
	   
	      while(x>0)
	      {
	         sum+= x%10;
	         x=x/10;
	      }
	      
	    boolean answer = (total % sum == 0)?true:false;
        
        return answer;
    }
}