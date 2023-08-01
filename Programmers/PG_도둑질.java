/*
[5, 1, 1, 3, 4, 3, 7] 

두가지 케이스

1. 첫번째를 선택하는 경우(두번째, 마지막 선택 불가)
[5, 5, (6, 5), (8, 6), (10, 8), (11, 10), (X, 11)]


2. 첫번째를 선택하지 않는 경우(두번째, 마지막 선택 가능)
[0, (1, 0), (1, 1), (4, 1), (5, 4), (7, 5), (12, 7)]


점화식
DP_T[i] = arr[i] + max(DP_N[i-1], DP_T[i-2], DP_N[i-2]);
DP_N[i] = max(DP_T[i-1], DP_N[i-1]);

*/


class Solution {
    public int solution(int[] money) {
        int answer = 0;
        int L = money.length;
        
        for (int t=0; t<2; t++) {
            int[] DP_T = new int[L];
            int[] DP_N = new int[L];
            // 첫번째를 선택하는 경우
            if (t == 0) {
                DP_T[0] = money[0];
                DP_N[1] = money[0];
                for (int i=2; i<L; i++) {
                    DP_N[i] = Math.max(DP_T[i-1], DP_N[i-1]);
                    if (i == L-1) continue;
                    DP_T[i] = money[i] + Math.max(DP_T[i-2], Math.max(DP_N[i-2], DP_N[i-1]));
                }
            }
            // 첫번째를 선택하지 않는 경우
            if (t == 1) {
                DP_T[1] = money[1];
                for (int i=2; i<L; i++) {
                    DP_N[i] = Math.max(DP_T[i-1], DP_N[i-1]);
                    DP_T[i] = money[i] + Math.max(DP_T[i-2], Math.max(DP_N[i-2], DP_N[i-1]));
                }                
            }
            // 최댓값
            answer = Math.max(answer, Math.max(DP_T[L-1], DP_N[L-1]));
        }
        
        return answer;
    }
}