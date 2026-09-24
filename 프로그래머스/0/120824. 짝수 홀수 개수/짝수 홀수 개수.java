class Solution {
     public int[] solution(int[] num_list) {
        int[] answer = {};
        int o_cnt = 0;
        int e_cnt = 0;
        for (int num : num_list) {
            if (num % 2 == 0) {
                e_cnt++;
            } else {
                o_cnt++;
            }
        }
        answer = new int[]{e_cnt, o_cnt};
        return answer;
    }
}