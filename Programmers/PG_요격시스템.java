/*
풀이
1. 폭격 미사일 정렬
- 정렬 기준 : e가 작은순으로
2. 폭격 미사일 순회
- 순회하면서 e보다 크거나 같은 s가 나오면 
    - cnt + 1
    - 비교기준값을 s의 e로 변경
*/

import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        // 정렬
        Arrays.sort(targets, (o1, o2) -> o1[1] - o2[1]);
        // 순회
        int std = -1;
        for (int[] target : targets) {
            if (target[0] >= std) {
                answer++;
                std = target[1];
            }
        }
        
        return answer;
    }
}