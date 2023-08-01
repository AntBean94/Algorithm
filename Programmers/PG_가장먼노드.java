import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i=0; i<n+1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int[] e : edge) {
            ArrayList<Integer> a = graph.get(e[0]);
            a.add(e[1]);
            graph.set(e[0], a);
            ArrayList<Integer> b = graph.get(e[1]);
            b.add(e[0]);
            graph.set(e[1], b);
        }
        
        return bfs(graph);
    }
    
    public int bfs(ArrayList<ArrayList<Integer>> graph) {
        int m = 0;
        
        Queue<Integer> q = new LinkedList<>();
        int[] visit = new int[graph.size()];
        q.add(1);
        visit[1] = 1;
        while (!q.isEmpty()) {
            int s = q.poll();
            for (int t : graph.get(s)) {
                if (visit[t] > 0) continue;
                visit[t] = visit[s] + 1;
                q.add(t);
                m = visit[t];
            }
        }
        
        int cnt = 0;
        for (int v : visit) {
            if (v == m) cnt++;
        }
        
        return cnt;
    }
}