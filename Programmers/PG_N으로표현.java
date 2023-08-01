import java.util.*;

class Solution {
    public int solution(int N, int number) {
        
        int[] DP = new int[100000];
        
        DP[N] = 1;
        int n = N;
        for (int i=2; i<6; i++) {
            n = n * 10 + N;
            DP[n] = i;
        }
        
        // 모든 수끼리 연산
        for (int k=0; k<2; k++) {
            for (int i=1; i<100000; i++) {
                if (DP[i] == 0) continue;
                // 10만 이상이거나 0이하인 경우 제외
                for (int j=i; j<100000; j++) {
                    if (DP[j] == 0) continue;
                    if (DP[i] + DP[j] > 8) continue;
                    // 덧셈
                    if (i + j < 100000) DP[i+j] = DP[i+j] == 0 ? DP[i] + DP[j] : Math.min(DP[i+j], DP[i] + DP[j]);
                    // 뺄셈
                    if (j - i > 0) DP[j-i] = DP[j-i] == 0 ? DP[i] + DP[j] : Math.min(DP[j-i], DP[i] + DP[j]);
                    // 곱셈
                    if (i * j < 100000) DP[i*j] = DP[i*j] == 0 ? DP[i] + DP[j] : Math.min(DP[i*j], DP[i] + DP[j]);
                    // 나눗셈
                    if (j / i > 0) DP[j/i] = DP[j/i] == 0 ? DP[i] + DP[j] : Math.min(DP[j/i], DP[i] + DP[j]);
                }

            }
        }
        
        return DP[number] == 0 ? -1 : DP[number];
    }
}