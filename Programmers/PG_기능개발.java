// 풀이
// 각 작업에 필요한 날짜를 기록
// 작업에 필요한 날짜를 순회
// 배포작업보다 작업날짜가 적거나 같으면 같이 배포

import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(0);
        int[] times = new int[speeds.length];
        // 잔여시간
        for (int i = 0; i < speeds.length; i++) {
            int r = 100 - progresses[i];
            times[i] = r / speeds[i] + ((r % speeds[i]) > 0 ? 1 : 0);
        }
        // 순회
        int d = times[0];
        int idx = 0;
        for (int time : times) {
            if (time > d) {
                answer.add(0);
                d = time;
                idx++;
            }
            answer.set(idx, answer.get(idx) + 1);
        }
        return answer;
    }
}