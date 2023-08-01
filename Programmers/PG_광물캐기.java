/*
문제
- 곡괭이 사용횟수는 5회(피로도 상관없이)
- 한번사용한 곡괭이는 계속 사용해야함

- picks [dia, iron, stone]

- 5개씩 끊어서 점수내기?
dia 1개는 25점
iron 1개는 5점
stone 1개는 1점

남은 곡괭이 iron
dia 1개 stone 4개 => 피로도 9
iron 5개 => 피로도 5

부분합, 그리디
*/
import java.util.*;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        
        // 피로도
        HashMap<String, Integer[]> fatigue = new HashMap<>();
        Integer[] dia = {1, 5, 25};
        Integer[] iron = {1, 1, 5};
        Integer[] stone = {1, 1, 1};
        fatigue.put("diamond", dia);
        fatigue.put("iron", iron);
        fatigue.put("stone", stone);
        
        // 5단위로 묶음
        int L = minerals.length;
        int capa = Math.min(Arrays.stream(picks).sum() * 5, L);
        int L5 = capa % 5 > 0 ? capa / 5 + 1 : capa / 5;
        int[][] points = new int[L5][2];
        
        // 가중치 입력
        int sum = 0;
        for (int i=1; i<= capa; i++) {
            sum += converter(minerals[i-1]);
            if (i % 5 == 0 || i == L) {
                points[(i - 1) / 5][0] = (i - 1) / 5;
                points[(i - 1) / 5][1] = sum;
                sum = 0;
            }
        }
        // 가중치 기준으로 정렬
        Arrays.sort(points, (o1, o2) -> o2[1] - o1[1]);
        int idx = 0;

        for (int i=0; i<3; i++) {
            int pick = picks[i];
            while (pick > 0 && idx < L5) {
                int targetIdx = points[idx++][0];
                int start = targetIdx * 5;
                for (int j=start; j<Math.min(start+5, L); j++) {
                    String cur = minerals[j];
                    answer += fatigue.get(cur)[i];
                }
                pick--;
            }
        }
        
        return answer;
    }
    
    public int converter(String mineral) {
        int cost = 0;
        if (mineral.equals("diamond")) cost = 25;
        if (mineral.equals("iron")) cost = 5;
        if (mineral.equals("stone")) cost = 1;
        return cost;
    }
}