/*
풀이

기준
거리가 n이려면 바위를 몇개 없애야하는지 확인
=> 조건을 만족하더라도 범위를 상단으로 좁혀서 가능한 큰 값을 만들어야함

거리를 만족하는 바위를 제거하는 로직
[0, 2, 11, 14, 17, 21, 25]
[2, 9, 3, 3, 4, 4]

*/

import java.util.*;

class Solution {
    
    private static int[] dist;
    
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        // 거리배열
        Arrays.sort(rocks);
        dist = new int[rocks.length + 1];
        for (int i=0; i<=rocks.length; i++) {
            if (i == 0) dist[i] = rocks[i];
            if (i > 0 && i < rocks.length) dist[i] = rocks[i] - rocks[i-1];
            if (i == rocks.length) dist[i] = distance - rocks[i-1];
        }
        
        // 이분탐색
        int l = 0;
        int r = distance;
        while (l <= r) {
            int mid = (l + r) / 2;
            // 제거한 바위의 수
            int result = check(mid);
            if (result <= n) {
                l = mid + 1;
                answer = mid;
            }
            if (result > n) {
                r = mid - 1;
            }
        }
        
        return answer;
    }
    
    public int check(int n) {
        int result = 0;
        
        int pre = 0;
        for (int d : dist) {
            pre += d;
            if (pre < n) {
                result++;
            } else {
                pre = 0;
            }
        }
        
        return result;
    }
}