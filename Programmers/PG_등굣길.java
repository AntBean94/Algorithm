/*
DP[i][j] = DP[i-1][j] + DP[i][j-1]

*/

class Solution {
    public int solution(int m, int n, int[][] puddles) {

        long[][] DP = new long[n][m];
        DP[0][0] = 1;
        for (int[] p : puddles) {
            DP[p[1]-1][p[0]-1] = -1;
        }
        
        for (int y=0; y<n; y++) {
            for (int x=0; x<m; x++) {
                if (DP[y][x] < 0) continue;
                long top = y == 0 ? 0 : (DP[y-1][x] > 0) ? DP[y-1][x] : 0;
                long left = x == 0 ? 0 : (DP[y][x-1] > 0) ? DP[y][x-1] : 0;
                DP[y][x] = (top + left + DP[y][x]) % 1000000007;
            }
        }
        
        return (int) DP[n-1][m-1];
    }
}