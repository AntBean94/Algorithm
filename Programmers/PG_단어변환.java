/*
단어의 차이가 한개인경우 변환가능

*/

import java.util.*;
import java.util.stream.Stream;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int cnt = words.length + 1;
        int lth = begin.length();
        int[][] maps = new int[cnt][cnt];
        String[] b = { begin };
        String[] allWords = Stream.of(b, words).flatMap(Stream::of).toArray(String[]::new);
        
        for (int i = 0; i < cnt; i++) {
            for (int j = i + 1; j < cnt; j++) {
                // 문자열 대조
                int c = 0;
                for (int k = 0; k < lth; k++) {
                    if (allWords[i].charAt(k) == allWords[j].charAt(k)) c++;
                }
                if (c == lth-1) {
                    maps[i][j] = 1;
                    maps[j][i] = 1;
                }
            }
        }
        
        return bfs(maps, cnt, target, allWords);
    }
    
    public int bfs(int[][] maps, int cnt, String target, String[] allWords) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        int[] visit = new int[cnt];
        q.add(0);
        visit[0] = 1;
        
        while (!q.isEmpty()) {
            int t = q.poll();
            if (allWords[t].equals(target)) {
                answer = visit[t];
                break;
            }
            for (int i = 0; i < cnt; i++) {
                if (i == t || visit[i] > 0 || maps[t][i] == 0) continue;
                q.add(Integer.valueOf(i));
                visit[i] = visit[t] + 1;
            }
        }
        
        return answer > 0 ? answer - 1 : answer;
    }
}