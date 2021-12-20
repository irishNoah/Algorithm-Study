class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        //int answer = 0;
        //return answer;
        //각 학생마다 몇 벌의 체육복이 있는지 확인하기 위한 배열 dress 선언
		int[] dress = new int[n];
        //처음에는 각 번호마다 체육복 1벌씩 있다고 가정
		for(int i = 0; i < n; i++) {
			// 각 인덱스마다 배열값을 1로 초기화
			dress[i] = 1;
		}
        
        /*
		//배열의 인덱스는 0부터 시작하므로
		//번호가 1,2,3,4,5번이라면
		//컴퓨터 상에서의 배열에는 0,1,2,3,4와 같다.  
		 */
		for(int i = 0; i < lost.length; i++) {
			lost[i] = lost[i]-1;
		}
		
		//잃어버린 번호의 학생은 체육복이 0벌이 됨.
		for(int i = 0; i < lost.length; i++) {
			for(int j = 0; j < n; j++) {
				if(j == lost[i]) {
					dress[j] -= 1;
				}
			}
		}
        
        /*
		//배열의 인덱스는 0부터 시작하므로
		//번호가 1,2,3,4,5번이라면
		//컴퓨터 상에서의 배열에는 0,1,2,3,4와 같다.  
		 */ 
		for(int i = 0; i < reserve.length; i++) {
			reserve[i] = reserve[i]-1;
		}
        
        /*
		//빌려줄 수 있는 번호의 학생은 체육복이 1벌 또는 2벌이 됨.
		//
		//빌려줄 수 있는 번호의 학생은 체육복이 1벌 또는 2벌이 됨.
		//도둑을 안 맞은 학생은 최대 2벌까지 될 수 있으며
		//도둑을 맞았으나 기존에 여벌이 있다면 1벌만 남게 된다. 
		//조건 : 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
		//이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
		//남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
		 */
		for(int i = 0; i < reserve.length; i++) {
			for(int j = 0; j < n; j++) {
				if(j == reserve[i]) {
					dress[j] += 1;
				}
			}
		}
        
        /*
		체육복이 아예 1벌도 없는 애가 양 옆의 번호 친구한테 빌리고 있는 과정
		단, 양옆 번호한테만 빌릴 수 있고, 양 옆 번호 학생도 가지고 있는 체육복의 수가 0,1개이면 빌리지 못한다.
		무조건 2벌 보유한 번호의 친구한테만 빌릴 수 있다. 
		 */
		for(int i = 0; i < n; i++) {
			//인덱스가 0인 경우는 왼쪽 인덱스(-1)가 없으므로
			//인덱스가 0인 친구는 인덱스가 1인 친구한테만 빌릴 수 있다.
			if(dress[i] == 0) {
				if(i == 0) {
					if(dress[i+1] == 2) {
						dress[i+1] = 1;
						dress[i] = 1;
					}
				}
				//인덱스가 마지막인 경우는 오른쪽 인덱스(n)이 없으므로
				//인덱스가 마지막인 친구는 인덱스가 n-2(이 for문 상에서는 i-1)인 친구한테만 빌릴 수 있다.
				else if(i == n-1) {
					if(dress[i-1] == 2) {
						dress[i-1] = 1;
						dress[i] = 1;
					}
				}
				//인덱스가 처음이거나 마지막이 아닌 경우의 인덱스는 양 옆 인덱스에게 빌릴 수 있다.
				else {
					if(dress[i-1] == 2) {
						dress[i-1] = 1;
						dress[i] = 1;
					}
					else if(dress[i+1] == 2) {
						dress[i+1] = 1;
						dress[i] = 1;
					}
				}
			}
		}
        
        //수업 들을 수 있는 학생 최대 수를 구하기 위한 변수 answer 선언
		int answer = 0;
		for(int i = 0; i < n; i++) {
			if(dress[i] > 0) {
				answer++;
			}
		}
        
        return answer;
        
    }
}