/*
조건
- 트리
- 노드(n) <= 100
- 간선(v) = n - 1

풀이
- 방문 배열 생성
- 간선을 하나씩 없앤 상황에서 순회

1. wires순회
2. i에 해당하는 간선을 제외하고 트리를 만듬
3. 방문 배열 생성
4. 노드를 순회하면서 bfs, 각 그룹별 갯수 체크
5. 그룹 갯수 리턴
*/

import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 100000000;
        
        for (int i = 0; i < wires.length; i++) {
            int gap = 0;
            ArrayList<ArrayList<Integer>> tree = new ArrayList<>();
            for (int k = 0; k <= n; k++) tree.add(new ArrayList<Integer>());
            
            // 트리 만들기
            for (int j = 0; j < wires.length; j++) {
                if (i == j) continue;
                int a = wires[j][0];
                int b = wires[j][1];
                ArrayList<Integer> treeA = tree.get(a);
                treeA.add(b);
                tree.set(a, treeA);
                ArrayList<Integer> treeB = tree.get(b);
                treeB.add(a);
                tree.set(b, treeB);
            }
            
            // 그래프 탐색(노드별 순회)
            boolean[] visit = new boolean[n+1];
            for (int j = 1; j <= n; j++) {
                if (visit[j]) continue;
                gap = Math.abs(gap - bfs(tree, visit, j));
            }
            
            answer = Math.min(answer, gap);
        }
        
        return answer;
    }
    
    public int bfs(ArrayList<ArrayList<Integer>> tree, boolean[] visit, int s) {
        int cnt = 1;
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(s);
        visit[s] = true;
        
        while (!queue.isEmpty()) {
            int t = queue.poll();
            ArrayList<Integer> list = tree.get(t);
            for (int k = 0; k < list.size(); k++) {
                int n = list.get(k);
                if (visit[n]) continue;
                queue.add(n);
                cnt++;
                visit[n] = true;
            }
        }
        
        return cnt;
    }
}