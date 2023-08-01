/*
1. 정수좌표 추출
2. y, x축 최솟값으로 모든 좌표 빼기
3. 문자열 변환 및 출력
*/

import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        
        // 정수 좌표 추출
        HashSet<long[]> loc = new HashSet<>();
        for (int i=0; i<line.length; i++) {
            for (int j=i+1; j<line.length; j++) {
                long a1 = line[i][0], b1 = line[i][1], c1 = line[i][2];
                long a2 = line[j][0], b2 = line[j][1], c2 = line[j][2];
                
                long mod = a1 * b2 - a2 * b1;
                if (mod == 0L) continue;
        
                long xNum = b1 * c2 - b2 * c1;
                long yNum = c1 * a2 - a1 * c2;
                
                if (xNum % mod != 0 || yNum % mod != 0) continue;
                
                long[] point = { yNum / mod, xNum / mod};
                loc.add(point);
            }
        }
        
        // 좌표 이동(최소값 기준)
        long minY = 200000000000L;
        long minX = 200000000000L;
        long maxY = -200000000000L;
        long maxX = -200000000000L;
        for (long[] p : loc) {
            minY = Math.min(minY, p[0]);
            minX = Math.min(minX, p[1]);
            maxY = Math.max(maxY, p[0]);
            maxX = Math.max(maxX, p[1]);
        }
        int ly = (int) (maxY - minY + 1L);
        int lx = (int) (maxX - minX + 1L);
        
        // 문자열 변환
        String[][] canvas = new String[ly][lx];
        for (int i=0; i<ly; i++) {
            for (int j=0; j<lx; j++) {
                canvas[i][j] = ".";
            }
        }
        for (long[] p : loc) {
            canvas[(int) (p[0] - minY)][(int) (p[1] - minX)] = "*";
        }
        
        String[] answer = new String[ly];
        for (int i=ly; i>0; i--) {
            answer[i-1] = "";
            for (int j=0; j<lx; j++) {
                answer[i-1] += canvas[ly-i][j];
            }
        }
        
        return answer;
    }
}