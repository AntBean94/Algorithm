/*
조건
- 원의 방정식(중심이 원점) => x^2 + y^2 = r^2
- 반지름은 정수

x범위를 0부터 r까지 잡고 순회
0일때 y가 가능한 범위는 0부터 r1의 
r1^2 - x^2 <= y^2 <= r2^2 - x^2

*/


class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        for (long x=1; x<=r2; x++) {
            double c = (x < r1) ? 1.0 * r1 * r1 - 1.0 * x * x : 0.0;
            long start = (int) Math.ceil(Math.sqrt(c));
            long end = (int) Math.floor(Math.sqrt(1.0 * r2 * r2 - 1.0 * x * x));
            answer += (end - start + 1);
        }
        
        return answer * 4;
    }
    
}