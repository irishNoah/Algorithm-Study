class Solution {
    public String solution(String phone_number) {
        char[] phone_CharArr = phone_number.toCharArray();
        for(int i = 0; i < phone_CharArr.length-4;i++) {
			phone_CharArr[i] = '*';
		}
        phone_number = String.valueOf(phone_CharArr);
        String answer = "";
        answer = phone_number;
        return answer;
    }
}