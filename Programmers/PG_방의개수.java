/*
풀이

간선체크
0,0to1,1
1,1to0,0
*/

import java.util.*;

class Solution {
    
    // 델타탐색
    private static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    private static int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
    
    public int solution(int[] arrows) {
        
        HashSet<String> node = new HashSet<>();
        HashSet<String> edge = new HashSet<>();
        node.add("0,0");
        int y = 0, x = 0;
        
        for (int a : arrows) {
            for (int k=0; k<2; k++) {
                int ny = y + dy[a];
                int nx = x + dx[a];
                // 노드 추가
                node.add(ny + "," + nx);
                // 간선 추가
                edge.add(y + "," + x + "to" + ny + "," + nx);
                edge.add(ny + "," + nx + "to" + y + "," + x);
                y = ny;
                x = nx;
            }
        }
        
        int answer = 1 + edge.size() / 2 - node.size();
        
        return answer > 0 ? answer : 0;
    }
}