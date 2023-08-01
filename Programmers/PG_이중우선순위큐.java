/* 풀이

필요자료구조
- 오름차순 우선순위큐
- 내림차순 우선순위큐
- 큐 카운터
- 해당 정수큐가 들어있는 갯수 체크

I연산: 넣는다.
D연산: 우선순위큐에서 뽑은 수가 실제 큐에 포함된 수인지 확인, 포함안되어있으면 다시 뽑는다.

*/


import java.util.PriorityQueue;
import java.util.HashMap;


class Solution {
    public int[] solution(String[] operations) {
        // 자료구조 정의
        PriorityQueue<Integer> maxQ = new PriorityQueue<>((o1, o2) -> o2 - o1);
        PriorityQueue<Integer> minQ = new PriorityQueue<>();
        HashMap<String, Integer> check = new HashMap<>();
        int cnt = 0;
        
        for (String operation : operations) {
            String[] cmd = operation.split(" ");
            if (cmd[0].equals("I")) {
                maxQ.offer(Integer.valueOf(cmd[1]));
                minQ.offer(Integer.valueOf(cmd[1]));
                if (check.containsKey(cmd[1])) check.put(cmd[1], check.get(cmd[1]) + 1);
                else check.put(cmd[1], 1);
                cnt++;
                continue;
            }
            
            if (cnt == 0) continue;
            
            if (cmd[0].equals("D") && cmd[1].equals("1")) deleteQueue(maxQ, check);
            if (cmd[0].equals("D") && cmd[1].equals("-1")) deleteQueue(minQ, check);
            cnt--;
        }
        
        int minValue = cnt >= 1 ? deleteQueue(minQ, check) : 0;
        int maxValue = cnt > 1 ? deleteQueue(maxQ, check) : minValue;
        
        return new int[] { maxValue, minValue };
    }
    
    public int deleteQueue(PriorityQueue<Integer> queue, HashMap<String, Integer> map) {
        int q;
        // 큐 삭제
        while (true) {
            q = queue.poll();
            String sq = Integer.toString(q);
            if (map.get(sq) > 0) {
                map.put(sq, map.get(sq) - 1);
                break;
            }
        }
        return q;
    }
}