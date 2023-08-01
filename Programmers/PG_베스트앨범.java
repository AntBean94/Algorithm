// 풀이
// 1. 맵1: 장르별 누적 재생횟수
// 2. 맵2: 장르별 우선순위 2개
// 장르가 같으면서 재생횟수가 같다면 인덱스가 작은값이 우선순위
// 500, 500, 500;
// 0, 2, 4
// 내림차순

import java.util.*;


class Solution {
    public ArrayList<Integer> solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();

        // id 정렬(재생횟수 우선순위)
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < plays.length; i++) hashmap.put(i, plays[i]);
        List<Map.Entry<Integer, Integer>> entries = new LinkedList<>(hashmap.entrySet());
        Collections.sort(entries, (id1, id2) -> id2.getValue().compareTo(id1.getValue()));
        
        int cnt = 0;
        int[] ids = new int[genres.length];
        for (Map.Entry<Integer, Integer> entry : entries) {
            ids[cnt++] = entry.getKey();
        }   
        
        // 장르별 누적 재생횟수
        HashMap<String, Integer> genMap = new HashMap<>();
        for (int i = 0; i < plays.length; i++) {
            if (genMap.containsKey(genres[i])) genMap.put(genres[i], genMap.get(genres[i]) + plays[i]);
            else genMap.put(genres[i], plays[i]);
        }
        List<Map.Entry<String, Integer>> entrieG = new LinkedList<>(genMap.entrySet());
        Collections.sort(entrieG, (gen1, gen2) -> gen2.getValue().compareTo(gen1.getValue()));
        
        HashMap<String, ArrayList<Integer>> gens = new HashMap<>();
        ArrayList<String> gen_sequence = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : entrieG) {
            gens.put(entry.getKey(), new ArrayList<>());
            gen_sequence.add(entry.getKey());
        }
        
        // 곡 담기
        for (int id : ids) {
            ArrayList<Integer> arr = gens.get(genres[id]);
            arr.add(id);
            gens.put(genres[id], arr);
        }
        
        for (String gen : gen_sequence) {
            int cnt2 = 0;
            for (Integer songId : gens.get(gen)) {
                if (cnt2 > 1) break;
                answer.add(songId);
                cnt2++;
            }
        }
        
        return answer;
    }
}