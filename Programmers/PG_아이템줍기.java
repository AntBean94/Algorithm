/*
풀이
- 맵을 만든다.
- 테두리가 1이고 가운데는 비어있는 맵
- 다른 사각형과 겹치는 테두리는 +1
- 1인 지점만 따라가도록 알고리즘 구현
*/

import java.util.*;
import java.awt.Point;

class Solution {
    
    // 상, 하, 좌, 우
    private int[] dy = {-1, 1, 0, 0};
    private int[] dx = {0, 0, -1, 1};
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        
        int[][] maps = new int[101][101];
        for (int[] coordinate : rectangle) {
            draw(maps, coordinate);
        }
        
        return bfs(maps, characterX * 2, characterY * 2, itemX * 2, itemY * 2) / 2;
    }
    
    
    public void draw(int[][] maps, int[] coor) {
        int ly = coor[1] * 2;
        int lx = coor[0] * 2;
        int ry = coor[3] * 2;
        int rx = coor[2] * 2;
        
        for (int i=ly; i<=ry; i++) {
            for (int j=lx; j<=rx; j++) {
                // 테두리만 1
                if (i == ly || i == ry || j == lx || j == rx) {
                    if (maps[i][j] > 1) continue;
                    maps[i][j] = 1;
                } else maps[i][j] = 2;
            }
        }
    }
    
    public int bfs(int[][] maps, int cX, int cY, int iX, int iY) {
        int distance = 0;
        
        Queue<Point> q = new LinkedList<>();
        int[][] visit = new int[101][101];

        q.add(new Point(cX, cY));
        visit[cY][cX] = 1;

        while (!q.isEmpty()) {
            Point p = q.poll();
            int y = (int) p.getY();
            int x = (int) p.getX();
            if (y == iY && x == iX) {
                distance = visit[y][x] - 1;
                break;
            }
            // 상하좌우 이동
            for (int i=0; i<4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (ny < 0 || ny > 100 || nx < 0 || nx > 100) continue;
                if (visit[ny][nx] > 0 || maps[ny][nx] != 1) continue;
                visit[ny][nx] = visit[y][x] + 1;
                q.add(new Point(nx, ny));
            }
        }
        
        return distance;
    }
}