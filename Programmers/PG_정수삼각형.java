/*

DP[i][n] = triangle[i][n] + max(DP[i-1][n-1], DP[i-1][n])

*/

class Solution {
    public int solution(int[][] triangle) {
        int lth = triangle.length;
        int[][] DP = new int[lth][lth];
        // 초기값
        DP[0][0] = triangle[0][0];
        
        for (int i=1; i<lth; i++) {
            for (int j=0; j<=i; j++) {
                if (j == 0) DP[i][j] = triangle[i][j] + DP[i-1][j]; 
                if (j == i) DP[i][j] = triangle[i][j] + DP[i-1][j-1];
                if (j != 0 && j != i) DP[i][j] = triangle[i][j] + Math.max(DP[i-1][j-1], DP[i-1][j]);
            }
        }
        
        int answer = 0;
        for (int i : DP[lth-1]) answer = Math.max(answer, i);
        return answer;
    }
}