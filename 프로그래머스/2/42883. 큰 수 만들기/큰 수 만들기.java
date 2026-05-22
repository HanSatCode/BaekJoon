import java.util.*;

class Solution {
    public String solution(String number, int k) {
        String answer = "";

        Deque<Character> deque = new ArrayDeque<>();
        for (char c : number.toCharArray()) {
            while(k > 0 && !deque.isEmpty() && deque.peekLast() < c) {
                deque.pollLast(); k--;
            }
            deque.addLast(c);
        }

        int size = deque.size();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < size - k; i++) {
            sb.append(deque.pollFirst());
        }
        answer = sb.toString();

        return answer;
    }
}