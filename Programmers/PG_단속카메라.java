/*
방문배열 하나
오른쪽이 작은순으로 정렬
routes 순회
- 출구보다 입구가 작거나 같은 케이스 체크
- 이미 방문했던 케이스는 스킵
*/

import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        int lth = routes.length;
        int[] visit = new int[lth];

        Arrays.sort(routes, (o1, o2) -> o1[1] - o2[1]);
        
        for (int i = 0; i < lth; i++) {
            if (visit[i] == 1) continue;
            visit[i] = 1;
            for (int j = i + 1; j < lth; j++) {
                if (visit[j] == 1) continue;
                if (routes[i][1] >= routes[j][0]) visit[j] = 1;
            }
            answer++;
        }
        
        return answer;
    }
}