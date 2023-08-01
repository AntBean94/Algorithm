/* 풀이
우선순위큐, 힙 자료구조 사용

반복문(while) 실행
- 데이터가 없으면 -1 return;
- 뽑은 첫번째 데이터 확인
- 조건을 만족하면 두번째 데이터 뽑아서 섞는다. cnt +1
- 조건을 만족하지 않으면 break

*/

import java.util.PriorityQueue;


class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        // 우선순위큐에 데이터 넣기
        for (Integer s : scoville) {
            pq.add(s);
        }
        
        int cnt = 0;
        // 반복문으로 섞기
        while (pq.peek() < K) {
            Integer x = pq.poll();
            
            // 두번째 값 존재여부 확인
            if (pq.isEmpty()) {
                cnt = -1;
                break;
            }
            
            Integer y = pq.poll();
            pq.add(x + y * 2);
                
            cnt++;
        }
        
        
        return cnt;
    }
}