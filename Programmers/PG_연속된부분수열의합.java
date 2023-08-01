/*
문제
- 비내림차순
*/

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        answer[1] = 100000000;
        
        int l = 0, r = 0;
        int total = sequence[l];
        while (r < sequence.length) {
            if (total == k) {
                if (answer[1] - answer[0] > r - l) {
                    answer[0] = l;
                    answer[1] = r;
                }
                r += 1;
                if (r >= sequence.length) break;
                total += sequence[r];
            }
            if (total < k) {
                r += 1;
                if (r >= sequence.length) break;
                total += sequence[r];
            }
            if (total > k) {
                total -= sequence[l];
                l += 1;
                if (l >= sequence.length) break;
            }
        }
        
        return answer;
    }
}