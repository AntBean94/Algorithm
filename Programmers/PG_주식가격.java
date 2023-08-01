/* 풀이
prices
현재 기준 가격이 떨어지지않은 기간은 몇초인지

조건1. 1 <= price <= 10,000
조건2. 2 <= prices.length <= 100,000

스택사용
[(값, 측정 시간)] 

스택의 탑과 price비교
price가 크거나 같으면 스택에 넣음
price가 더 작으면 스택에서 price보다 작거나 같은값이 나올때까지 뺀다.
스택에서 뺄때
- 입장시간을 index
- (현재시간 - 입장시간 + 1)을 value

stack: push, pop, peek 등
*/

import java.util.Stack;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<ArrayList<Integer>> stack = new Stack<>();
        
        int time = 0;
        // 순회
        for (int price : prices) {
            ArrayList<Integer> s = new ArrayList<>();
            s.add(price);
            s.add(time);
            while (true) {
                if (stack.empty()) {
                    stack.push(s);
                    break;
                }
                // 스택 최상단값이 더 크다면(감소)
                if (stack.peek().get(0) > s.get(0)) {
                    ArrayList<Integer> ns = stack.pop();
                    answer[ns.get(1)] = time - ns.get(1);
                } else {
                    stack.push(s);
                    break;
                }                            
            }
            time++;
        }
        // 남은 스택에서 빼내기
        while (true) {
            if (stack.empty()) break;
            ArrayList<Integer> ns = stack.pop();
            answer[ns.get(1)] = time - ns.get(1) - 1;
        }
        
        char var1 = 65;
        System.out.println(var1 == 'A');
        
        return answer;
    }
}