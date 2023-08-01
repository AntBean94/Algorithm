// 순회
import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int l = priorities.length;
        
        // 우선순위 체크리스트
        int[] cnt = new int[10];
        for (int p : priorities) {
            cnt[p]++;
        }
        
        // 우선순위별 확인
        int idx = 0;
        for (int i = 9; i >= 0; i--) {
            int c = cnt[i];
            while (c > 0) {
                // 비교 
                if (priorities[idx] == i) {
                    c--;
                    answer++;
                    if (location == idx) return answer;
                }
                
                // 인덱스 변경
                idx++;
                if (idx == l) idx = 0;
            }
        }
        
        return answer;
    }
}