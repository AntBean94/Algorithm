// 풀이
// 1. 해시맵 사용
// 2. 2차원배열 순회하며 의상종류별 갯수 체크
// 3. 의상 종류별 갯수 + 1 한뒤에 경우의 수 곱연산 (옷을 입지 않는 경우의 수 포함, 모두 벗는 경우의 수 제외) 
// ex) (a + 1) * (b + 1) * (c + 1) - 1

import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        for (String[] c : clothes) {
            if (map.containsKey(c[1])) map.put(c[1], map.get(c[1]) + 1);
            else map.put(c[1], 1);
        }
        for (Integer cnt : map.values()) answer *= (cnt + 1);
        return answer - 1;
    }
}