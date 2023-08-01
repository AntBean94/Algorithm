// 최단거리 bfs

import java.util.*;

class Solution {
    
    // 상, 하, 좌, 우
    private int[] dx = {0, 0, -1, 1};
    private int[] dy = {-1, 1, 0, 0};
    private static int Y;
    private static int X;
    
    public int solution(int[][] maps) {
        Y = maps.length;
        X = maps[0].length;
        int[][] visit = new int[Y][X];
        visit[Y-1][X-1] = -1;
        bfs(maps, visit);
        return visit[Y-1][X-1];
    }
    
    public void bfs(int[][] maps, int[][] visit) {
        
        Queue<int[]> queue = new LinkedList<>();
        int[] first = {0, 0};
        queue.add(first);
        visit[0][0] = 1;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int y = cur[0];
            int x = cur[1];
            for (int i=0; i<4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (ny >= 0 && ny < Y && nx >= 0 && nx < X && maps[ny][nx] > 0 && visit[ny][nx] < 1) {
                    int[] nxt = {ny, nx};
                    queue.add(nxt);
                    visit[ny][nx] = visit[y][x] + 1;
                }
            }
        }
        
    }
}