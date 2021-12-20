class Solution {
    public String solution(int n) {
        String answer = "";
    
        char[] arrS = {'수','박'};
        int nLeng = n;
        
        //추후에 answer리턴할 때 배열을 문자열로 변경해줄 예정
		char[] arrSToString = new char[nLeng];
		
		int k = 0;
		if(nLeng % 2 ==0) {//nLeng이 짝수라면
			for(int i = 0; i  < nLeng/2; i++) {
				for(int j = 0; j < 2; j++) {
					//System.out.print(arrS[j]);
					arrSToString[k] = arrS[j];
					k++;
				}
			}
            answer = String.valueOf(arrSToString);
        } 
        
        else {//nLeng이 홀수라면
			for(int i = 0; i  < nLeng/2; i++) {
				for(int j = 0; j < 2; j++) {
					//System.out.print(arrS[j]);
					arrSToString[k] = arrS[j];
					k++;
				}
			}
			arrSToString[nLeng-1] = '수';
			answer = String.valueOf(arrSToString);
		}
         return answer;
    }
}