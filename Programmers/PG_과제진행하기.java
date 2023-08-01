/*
풀이
- 스택자료구조 사용
- 문제를 시작시간에 따라 정렬
- 작업의 잔여시간 표기용 맵 자료구조
*/

import java.util.*;

class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        int idx = 0;
        
        // 정렬
        Arrays.sort(plans, (o1, o2) -> {
            int h1 = Integer.parseInt(o1[1].split(":")[0]);
            int m1 = Integer.parseInt(o1[1].split(":")[1]);
            int h2 = Integer.parseInt(o2[1].split(":")[0]);
            int m2 = Integer.parseInt(o2[1].split(":")[1]);
            if (h1 != h2) return h1 - h2;
            else return m1 - m2;
        });
        
        // 맵
        HashMap<String, Integer> time = new HashMap<>();
        for (String[] plan : plans) time.put(plan[0], Integer.valueOf(plan[2]));
        // 스택
        Stack<String> stack = new Stack<>();
        
        // 순회
        int now = 0;
        for (String[] plan : plans) {
            if (stack.isEmpty()) {
                stack.add(plan[0]);
                now = converter(plan[1]);
            } else {
                // 작업을 완료한만큼 빼기
                int nxt = converter(plan[1]);
                int diff = nxt - now;
                while (diff > 0 && !stack.isEmpty()) {
                    String cur = stack.peek();
                    int remain = time.get(cur);
                    if (remain <= diff) {
                        answer[idx++] = stack.pop();
                        diff -= remain;
                    } else {
                        time.replace(cur, remain - diff);
                        diff = 0;
                    }
                }
                // 다음 작업
                stack.add(plan[0]);
                now = nxt;
            }
        }
        // 스택작업 이후
        while (!stack.isEmpty()) {
            answer[idx++] = stack.pop();
        }
        
        return answer;
    }
    
    public int converter(String time) {
        String[] timeArr = time.split(":");
        int h = Integer.parseInt(timeArr[0]) * 60;
        int m = Integer.parseInt(timeArr[1]);
        return h + m;
    }
}