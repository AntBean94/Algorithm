/** 풀이
1. 두개의 큐(트럭무게, 트럭 들어간시간)
2. 대기트럭을 큐에 넣는다.(대기가 없을때까지)
    - 무게가 초과하지 않으면: 
        무게큐/시간큐(현재시간+1)에 추가
    - 무게가 초과한다면:
        무게/시간큐에서 뺀다, 시간 = 시간큐+다리길이
3. 대기큐를 다빼고 현재시간 업데이트
*/

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int now = 0;
        int total = 0;
        int idx = 0;
        int truck_cnt = truck_weights.length;
        Queue<Integer> bridge = new LinkedList<>();
        Queue<Integer> times = new LinkedList<>();
        // 트럭을 넣는다.
        while (idx < truck_cnt) {
            // 시간별로 들어오는애 나가는애가 있는지 확인
            int w = truck_weights[idx];
            
            // 트럭이 들어가는 경우
            if (w + total <= weight) {
                bridge.add(w);
                times.add(++now);
                idx++;
                total+=w;
                // 들어가면서 나오는 경우
                if (times.peek() + bridge_length == now) {
                    total-=bridge.poll();
                    times.poll();
                }
            } else {
            // 트럭이 안들어가는 경우
                total-=bridge.poll();
                now = bridge_length + times.poll();
                // 빼면서 들어가는지 확인
                if (w + total <= weight) {
                    bridge.add(w);
                    times.add(now);
                    idx++;
                    total+=w;
                }
            }
        }
        
        // 다리에서 모두 제거하면서 시간 업데이트
        while (total > 0) {
            total-=bridge.poll();
            now = bridge_length + times.poll();
        }
        
        return now;
    }
}