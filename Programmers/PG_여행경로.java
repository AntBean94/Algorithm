/*
- dfs
- 경로선택
*/

import java.util.*;

class Solution {
    
    int[][] maps;
    String[][] ticketsA;
    String[] routes = null;
    
    public String[] solution(String[][] tickets) {
        
        int cnt = tickets.length;
        Arrays.sort(tickets, (o1, o2) -> o1[1].compareTo(o2[1]));
        ticketsA = tickets;
        maps = new int[cnt][cnt];
        for (int i=0; i<cnt; i++) {
            for (int j=i+1; j<cnt; j++) {
                if (tickets[i][1].equals(tickets[j][0])) maps[i][j] = 1;
                if (tickets[j][1].equals(tickets[i][0])) maps[j][i] = 1;
            }
        }
        
        String[] answer;
        for (int i=0; i<cnt; i++) {
            if (ticketsA[i][0].equals("ICN")) {
                int[] visit = new int[cnt];
                visit[i] = 1;
                dfs(visit, i, "ICN " + ticketsA[i][1], 1);
                if (routes != null) break;         
            }
        }
        
        return routes;
    }
    
    public void dfs(int[] visit, int start, String cur, int cnt) {
        if (cnt == maps.length && routes == null) {
            routes = cur.split(" ");
            return;
        }
        
        for (int i=0; i<maps.length; i++) {
            if (visit[i] > 0 || maps[start][i] == 0 || start == i) continue;
            visit[i] = 1;
            dfs(visit, i, cur+" "+ticketsA[i][1], cnt+1);
            visit[i] = 0;
        }
    }
}