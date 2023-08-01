/*
풀이
union-find

1. costs를 건설비용(cost[2])기준으로 오름차순 정렬
2. 간선을 순회하며 union-find 알고리즘 실행
    - 부모가 같은경우 skip
    - 부모가 다른경우 결합하고 카운팅
    - 카운트가 n과 같으면 stop
*/

import java.util.*;


class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int cnt = 0;
        int[] parent = new int[n+1];
        for (int i = 0; i <= n; i++) parent[i] = i;
        
        Arrays.sort(costs, (o1, o2) -> {
            return o1[2] - o2[2];
        });
        
        for (int[] cost : costs) {
            int x = cost[0], y = cost[1], z = cost[2];
            if (!findParent(parent, x, y)) {
                unionParent(parent, x, y);
                answer += z;
                if (cnt++ == n) break;
            }
        }
        
        return answer;
    }
    
    public int getParent(int[] parent, int x) {
        if (parent[x] == x) return x;
        parent[x] = getParent(parent, parent[x]);
        return parent[x];
    }
    
    public void unionParent(int[] parent, int x, int y) {
        int a = getParent(parent, x);
        int b = getParent(parent, y);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }
    
    public boolean findParent(int[] parent, int x, int y) {
        int a = getParent(parent, x);
        int b = getParent(parent, y);
        if (a == b) return true;
        else return false;
    }
    
}