class Solution {
    public String solution(int[] numbers, String hand) {
        //무슨 손을 사용하여 번호를 눌렀는지 알기 위한 char형 배열 usingHand 선언
		char[] usingHand = new char[numbers.length];
        
        //처음에 왼손과 오른손의 위치가 각각 *과 #에 있음으로 String형 배열을 선언하려고 했으나.
		//사실 상 가운데 번호와 왼손 및 오른손의 현재 위치 사이의 거리를 구해 가운데 번호를 무슨 손으로 눌려야 하는지 알아야 하므로
		//2차원 int형 배열인 KeyPad선언 여기서 100과 200은 각각 *과 #의 역할이라고 생각하면 된다.
		int[][] keyPad = {{1,2,3}, {4,5,6}, {7,8,9}, {100, 0, 200}};
        
        	//거리를 구하고자 할 때 사용
		//changeJ1 왼손의 행, changeJ2는 오른손의 행 
		int changeJ1 = 3, changeJ2 = 3; 
		//changeK1 왼손의 열, changeK2는 오른손의 열 
		int changeK1 = 0, changeK2 = 2; 
		//distanceJ1,distanceK1은 가운데 번호와 현재 왼손 위치의 각각 행, 열인덱스 값을 빼서 거리를 구하기 위해 선언
		int distanceJ1 = 0, distanceK1 = 0;
		//distanceJ2,distanceK2은 가운데 번호와 현재 오른손 위치의 각각 행, 열인덱스 값을 빼서 거리를 구하기 위해 선언
		int distanceJ2 = 0, distanceK2 = 0;
        
        for(int i = 0; i < numbers.length; i++) {
			for(int j = 0; j < 4; j++) {//여기서 j는 keyPad 2차원 배열의 행 역할
				for(int k = 0; k < 3; k++) {//여기서 k는 keyPad 2차원 배열의 열 역할
			
					int sumJK1 = 0, sumJK2 = 0;
					
					if(numbers[i] == 2 || numbers[i] == 5 || numbers[i] == 8 || numbers[i] == 0) {
						//2,5,8,0는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용한다.
						if(numbers[i] == keyPad[j][k]) {
							//왼손과 가운데 번호 사이의 거리 구하기
							distanceJ1 = Math.abs(j-changeJ1);
							distanceK1 = Math.abs(k - changeK1); 
							sumJK1 = distanceJ1 + distanceK1;
							
							//오른손과 가운데 번호 사이의 거리 구하기
							distanceJ2 = Math.abs(j-changeJ2);
							distanceK2 = Math.abs(k-changeK2);
							sumJK2 = distanceJ2 + distanceK2;
							
							
							if(sumJK1 == sumJK2) {
								if(hand.equals("left")) {
									usingHand[i] = 'L';
									//다음 숫자도 가운데 열 번호일 수 있으므로, 현재 j와 k를
									//changeJ1, changeK1에 각각 대입
									changeJ1 = j;
									changeK1 = k;
								}
								else {
									usingHand[i] = 'R';
									//다음 숫자도 가운데 열 번호일 수 있으므로, 현재 j와 k를
									//changeJ2, changeK2에 각각 대입
									changeJ2 = j;
									changeK2 = k;
								}
							} 
							
							//sumJK2보다 sumJK1가 작으면 sumJK1가 더 가운데 번호에 가까움으로 왼손으로 누름
							else if(sumJK1 < sumJK2) {
								usingHand[i] = 'L';
								
								//다음 숫자도 가운데 열 번호일 수 있으므로, 현재 j와 k를
								//changeJ1, changeK1에 각각 대입
								changeJ1 = j;
								changeK1 = k;
							}
							//sumJK1보다 sumJK2가 작으면 sumJK2가 더 가운데 번호에 가까움으로 오른손으로 누름
							else {//else if(sumJK1 > sumJK2)
								usingHand[i] = 'R';
								//다음 숫자도 가운데 열 번호일 수 있으므로, 현재 j와 k를
								//changeJ2, changeK2에 각각 대입
								changeJ2 = j;
								changeK2 = k;
							}
							
						}
					}
					
					else if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
						//1,4,7은 무조건 왼손으로만 누른다.
						usingHand[i] = 'L';
						
						if(numbers[i] == keyPad[j][k]) {
							//numbers[i]의 값과 keyPad[j][k]일 경우
							//changeJ1에 j 값을, changeK1에 k 값을 대입
							changeJ1 = j;
							changeK1 = k;
						}
					}
					
					else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
						//3,6,9는 무조건 오른손으로만 누른다.
						usingHand[i] = 'R';
						
						if(numbers[i] == keyPad[j][k]) {
							//numbers[i]의 값과 keyPad[j][k]일 경우
							//changeJ2에 j 값을, changeK2에 k 값을 대입
							changeJ2 = j;
							changeK2 = k;
						}
					}
					
					
					
				}
			}
		}
        
       //char형 배열값을 String 형으로 변환하려고 한다면 
		//String 변수명 = new String(char형 배열 변수명);
		//이런 식으로 선언한다면 된다.
		String answer = new String(usingHand);
        
        return answer;
    }
}