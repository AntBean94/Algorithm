/*
풀이
- 금,은 범위 => 10억
- 도시의수 => 10만
- 시간 => 10만
=> 이분탐색

결정함수
g1 + s1 = t1
g2 + s2 = t2
    :
    :
gn + sn = tn
-------------
g_total > g_needs
s_total > s_needs
t_total >= g_needs + s_needs
=> 금을 옮기는데 사용한 필수자원 이외에는 은을 옮기는데 사용

*/


class Solution {
    public long solution(int a, int b, int[] g, int[] s, int[] w, int[] t) {
        long answer = -1;
        
        // parametric search
        long r = 400000000000000L;
        long l = 0L;
        while (l <= r) {
            long mid = (r + l) / 2;
            
            // dicisioin function
            long gold = 0, silver = 0, total = 0;
            for (int i=0; i<g.length; i++) {
                // 계산식 t
                long c = (mid / t[i] + 1) / 2 * w[i];
                gold += Math.min(g[i], c);
                silver += Math.min(s[i], c);
                total += Math.min(g[i] + s[i], c);
            }
            
            // find minimum
            if (gold >= a && silver >= b && total >= a + b) {
                r = mid - 1;
                answer = mid;
            } else {
                l = mid + 1;
            }
            
        }
        
        return answer;
    }
}