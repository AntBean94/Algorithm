class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visit = new int[n];
        
        for (int i = 0; i < computers.length; i++) {
            if (visit[i] == 1) continue;
            dfs(computers, visit, i);
            answer++;
        }
        
        return answer;
    }
    
    public void dfs(int[][] computers, int[] visit, int idx) {
        for (int i = 0; i < computers.length; i++) {
            if (visit[i] == 1) continue;
            if (computers[idx][i] == 0) continue; 
            visit[i] = 1;
            dfs(computers, visit, i);
        }
    }
}