/*
total = brown + yellow

yellow + brown = x * y 
brown/2 + 2 = x + y

*/


class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int total = brown + yellow;
        int std = brown / 2 + 2;
        for (int i = std - 1; i >= std / 2; i--) {
            int j = std - i;
            if (i * j == total) {
                answer[0] = i;
                answer[1] = j;
                break;
            }
        }
        
        return answer;
    }
}