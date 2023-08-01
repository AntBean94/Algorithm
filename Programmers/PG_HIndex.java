/*
문제
h-index구하기

풀이
- 내림차순 정렬
- 순회
    - 인덱스가 배열의값보다 작거나 같은 마지막 케이스의 인덱스 리턴(인덱스 +1)

9 8 7 6 6 5
1 2 3 4 5 6

*/

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] arr = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, Collections.reverseOrder());
        
        for (int i = 0; i < arr.length; i++) {
            if (i < arr[i] && arr[i] != 0) answer++;
            else break;
        }
        
        return answer;
    }
}