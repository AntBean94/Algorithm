/*
힌트
+ 는 결합법칙 성립  => +부호 순서상관 없음
- 는 결합법칙 성립X => -부호 순서상관 있음

5 - 3 + 1 - 2 - 4 = 7
5 - ((3 + (1 - 2)) - 4) = 7
5 - (((3 + 1) - 2) - 4) = 7

5  2  3  3  7
0 -3 -4 -2  2
0  0  1 -1  3
0  0  0 -2  2
0  0  0  0 -4

1 -2 -7  1
0 -3 -8  0
0  0  5 -3
0  0  0 -8

*/

import java.util.*;

class Solution {
    public int solution(String arr[]) {
        int INF = 1000000;
        int lth = arr.length / 2 + 1;
        int[][] MAX_DP = new int[lth][lth];
        int[][] MIN_DP = new int[lth][lth];        
        
        for (int k=0; k<lth; k++) {
            for (int i=0; i<lth-k; i++) {
                int j = i + k;
                MAX_DP[i][j] = -INF;
                MIN_DP[i][j] = INF;
                
                if (k == 0) {
                    int n = Integer.parseInt(arr[i*2]);
                    MAX_DP[i][j] = n;
                    MIN_DP[i][j] = n;
                    continue;
                }
                
                for (int t=i; t<j; t++) {
                    String flag = arr[t*2+1];
                    if (flag.equals("+")) {
                        MAX_DP[i][j] = Math.max(MAX_DP[i][j], MAX_DP[i][t] + MAX_DP[t+1][j]);
                        MIN_DP[i][j] = Math.min(MIN_DP[i][j], MIN_DP[i][t] + MIN_DP[t+1][j]);
                    } else {
                        MAX_DP[i][j] = Math.max(MAX_DP[i][j], MAX_DP[i][t] - MIN_DP[t+1][j]);
                        MIN_DP[i][j] = Math.min(MIN_DP[i][j], MIN_DP[i][t] - MAX_DP[t+1][j]);
                    }
                }
            }
        }
        
        return MAX_DP[0][lth-1];
    }
}