/*

시간복잡도 2^20 약 1,000,000

*/

class Solution {
    
    private static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, target, 0, 0);
        
        return answer;
    }
    
    public void dfs(int[] nums, int target, int idx, int cur) {
        if (idx == nums.length) {
            if (target == cur) answer++;
            return;
        }
        
        dfs(nums, target, idx + 1, cur + nums[idx]);
        dfs(nums, target, idx + 1, cur - nums[idx]);
    }
}