/*
brute-force
*/

class Solution {
    
    public int solution(int k, int[][] dungeons) {
        int[] visit = new int[dungeons.length];
        return dfs(dungeons, visit, k);
    }
    
    public int dfs(int[][] dungeons, int[] visit, int change) {
        int cnt = 0;
        for (int i = 0; i < dungeons.length; i++) {
            if (visit[i] == 1 || dungeons[i][0] > change) continue;
            visit[i] = 1;
            cnt = Math.max(dfs(dungeons, visit, change - dungeons[i][1]) + 1, cnt);    
            visit[i] = 0;
        }
        return cnt;
    }
    
}