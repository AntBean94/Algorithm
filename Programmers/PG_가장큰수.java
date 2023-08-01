/* 
문제
주어진 숫자를 조합해 가장 큰 수 리턴
조건1. 배열의 길이는 100,000
조건2. 각 수는 최대 1000
조건3. 정답은 문자열로 바꾸어 return

풀이
그리디
- 각 수의 위치를 바꿔서 합치고 대소비교
- 부분의 결과가 전체 결과와 같음
*/ 

import java.util.stream.Collectors;
import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        List<Integer> list = Arrays.stream(numbers).boxed().collect(Collectors.toList());
        
        list.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                String S1 = String.valueOf(o1);
                String S2 = String.valueOf(o2);
                // 그리디알고리즘
                int M1 = Integer.parseInt(S1 + S2);
                int M2 = Integer.parseInt(S2 + S1);
                return M2 - M1;
            }
        });
        
        for (int number : list) {
            answer += number;
        }
        // 0들의 배열일경우 0리턴
        if (answer.charAt(0) == '0') answer = "0";
        
        return answer;
    }
    
}