// 스택 자료구조 사용(push, pop, peek)

import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            Character b = s.charAt(i);
            if (b == ')') {
                if (stack.empty() || stack.peek() == ')') return false;
                else stack.pop();
            } else stack.push('(');
        }
        return stack.empty() ? true : false;
    }
}