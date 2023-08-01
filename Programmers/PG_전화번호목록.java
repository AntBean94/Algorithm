// 풀이
// 1. 문자열 정렬(아스키 순서, 오름차순)
// 2. 배열을 순회하며 i인덱스값과 i+1인덱스값이 포함관계인지 확인(String.startsWith())

import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (int i = 0; i < phone_book.length - 1; i++) {
            String now = phone_book[i];
            String nxt = phone_book[i+1];
            if (nxt.startsWith(now)) return false;
        }
        return true;
    }
}