/*
풀이
- 2차원배열
- 이긴선수 1
- 진선수 -1
- 그래프탐색 -> 이긴선수 + 진선수 = n-1이면 cnt+1
*/

import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        int[][] game = new int[n+1][n+1];
        for (int[] r : results) {
            game[r[0]][r[1]] = 1;
            game[r[1]][r[0]] = -1;
        }
        
        for (int i=1; i<n+1; i++) {
            int win_game = bfs(1, i, game);
            int lose_game = bfs(-1, i, game);
            if (win_game + lose_game == n-1) answer++;
        }
        
        return answer;
    }
    
    public int bfs(int std, int n, int[][] game) {
        int cnt = 0;
        
        int[] visit = new int[game.length];
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        visit[n] = 1;
        while (!q.isEmpty()) {
            int s = q.poll();
            for (int i=1; i<game.length; i++) {
                if (visit[i] > 0 || game[s][i] != std) continue;
                visit[i] = 1;
                q.add(i);
                cnt++;
            }
        }
        
        return cnt;
    }
}