/*
풀이

에라토스테네스의 체
완전탐색

*/

import java.util.*;


class Solution {
    
    private static int[] primeArray = new int[10000000];
    
    public Solution() {
        for (int i = 0; i < 10000000; i++) primeArray[i] = 1;
        eratosthenes();
    }
    
    public void eratosthenes() {
        for (int i = 2; i < 10000000; i++) {
            if (primeArray[i] == 0) continue;
            int k = i * 2;
            while (k < 10000000) {
                primeArray[k] = 0;
                k += i;
            }
        }
    }
    
    public void bruteforce(String[] nums, int[] visit, Set<Integer> set, String cur, int cnt) {
        // 재귀 탈출
        if (cnt == visit.length && cur.length() != 0) {
            set.add(Integer.valueOf(cur));
            return;
        };
        
        for (int i = 0; i < visit.length; i++) {
            if (visit[i] == 1) continue;
            visit[i] = 1;
            bruteforce(nums, visit, set, cur + nums[i], cnt + 1);
            bruteforce(nums, visit, set, cur, cnt + 1);
            visit[i] = 0;
        }        
    }
    
    public int solution(String numbers) {
        // 방문배열 선언 및 초기화
        int[] visit = new int[numbers.length()];
        for (int i = 0; i < numbers.length(); i++) visit[i] = 0;
        
        // 모든 경우의 수
        String[] arr = numbers.split("");
        Set<Integer> set = new HashSet<>();
        bruteforce(arr, visit, set, "", 0);
        
        // 소수판별
        int answer = 0;
        Iterator<Integer> iter = set.iterator();
        while (iter.hasNext()) {
            int num = iter.next();
            if (num == 0 || num == 1) continue;
            answer += primeArray[num];
        }
        
        return answer;
    }
}