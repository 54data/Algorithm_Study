class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for (int i = 0; i < my_string.length(); i++) {
            if (my_string.indexOf(my_string.charAt(i)) == my_string.lastIndexOf(my_string.charAt(i))) {
                answer += my_string.charAt(i);
            } else {
                if (answer.indexOf(my_string.charAt(i))==-1) {
                    answer += my_string.charAt(i);
                }
            }
        }
        return answer;
    }
}