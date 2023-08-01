import java.util.HashMap;

class Solution {
    
    private HashMap<String, Integer> map = new HashMap<>();
    
    public Solution() {
        map.put("A", 0);
        map.put("B", 1);
        map.put("C", 2);
        map.put("D", 3);
        map.put("E", 4);
        map.put("F", 5);
        map.put("G", 6);
        map.put("H", 7);
        map.put("I", 8);
        map.put("J", 9);
        map.put("K", 10);
        map.put("L", 11);
        map.put("M", 12);
        map.put("N", 13);
        map.put("O", 12);
        map.put("P", 11);
        map.put("Q", 10);
        map.put("R", 9);
        map.put("S", 8);
        map.put("T", 7);
        map.put("U", 6);
        map.put("V", 5);
        map.put("W", 4);
        map.put("X", 3);
        map.put("Y", 2);
        map.put("Z", 1);
    }
    
    public int solution(String name) {
        int answer = 0;
        int lth = name.length();
        int cnt = 0;
        int[] distR = new int[lth+1];
        int[] distL = new int[lth+1];
        String[] arr = name.split("");
        for (int i = 0; i < lth; i++) {
            answer += map.get(arr[i]);
            // 좌우 이동 최적화 알고리즘(1)
            if (i != 0 && !arr[i].equals("A")) {
                cnt++;
                distR[i] = 1;
                distL[lth-i] = 1;
            }
        }
        // 좌우 이동 최적화 알고리즘(2)
        int dL = 0;
        int dR = 0;
        int dM = 0;
        int mcnt = 0;
        for (int i = 1; i < lth; i++) {
            if (dM == 0 && distL[i] > 0 && distR[i] > 0 && mcnt + 2 > cnt) {
                dM = Math.min(dL, dR) * 2 + i;
            }
            if (distL[i] > 0) {
                dL = i;
                mcnt++;
            }
            if (distR[i] > 0) {
                dR = i;   
                mcnt++;
            }
            if (dM == 0 && cnt == mcnt) {
                dM = Math.min(dL, dR) * 2 + i;
            }
        }
        return answer + Math.min(Math.min(dR, dL), dM);
    }
}