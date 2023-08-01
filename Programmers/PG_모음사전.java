class Solution {
    
    private static int cnt = 0;
    private static int answer = 0;
    private String[] arr = {"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        solve(word, "");
        return answer;
    }
    
    public void solve(String word, String now) {
        if (now.length() == 5) return;
        
        for (int i = 0; i < 5; i++) {
            cnt++;
            if ((now + arr[i]).equals(word)) {
                answer = cnt;
                return;
            }
            solve(word, now + arr[i]);
        }
    }
}