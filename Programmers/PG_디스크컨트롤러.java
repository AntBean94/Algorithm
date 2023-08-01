/* 풀이

하나를 처리하는데 소요되는 비용은
기회비용(가중치) = 처리시간 + 대기시간(= 타겟프로세스 완료시점 - 대기프로세스 요청시점)

jobs 시간순으로 정렬
for 시간
    해당 시간대 job 추출
    작업들 우선순위큐에 넣기
    하나 추출 및 시간 업데이트

주의) 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
*/

import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

class Solution {
    public int solution(int[][] jobs) {
        
        // 시간순 정렬
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        
        // 우선순위큐 선언
        PriorityQueue<int []> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        int total_time = 0;
        int now = 0;
        int job_idx = 0;
        int job_cnt = jobs.length;
        // 현재시간 기준
        while (true) {
            // 요청시간 뽑기
            for (int i = job_idx; i < job_cnt; i++) {
                if (now < jobs[i][0]) break;
                job_idx++;
                pq.add(jobs[i]);
            }
            // 작업처리
            if (pq.isEmpty()) now++;
            else {
                int[] job = pq.poll();
                now += job[1];
                total_time += (now - job[0]);
                System.out.println(total_time);
            }
                
            // 모든 작업이 완료되면 종료
            if (job_idx == job_cnt && pq.isEmpty()) break;
        }
        return total_time / job_cnt;
    }
}