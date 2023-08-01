import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0L;
        
        long l = 0L;
        long r = (long) 1e18;
        while (l <= r) {
            long mid = (l + r) / 2;
            long result = check(mid, times);
            
            if (result >= n) {
                answer = mid;
                r = mid - 1;
            }
            if (result < n) {
                l = mid + 1;
            }
        }
        
        return answer;
    }
    
    public long check(long n, int[] times) {
        long result = 0L;
        for (int time : times) {
            result += n / time;
        }
        return result;
    }
}