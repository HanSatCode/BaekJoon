import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        Arrays.sort(routes, (a, b) -> a[1] - b[1]);
        int boundR = routes[0][1];
        for(int i = 1 ; i < routes.length; i++) {
            if(boundR < routes[i][0]) { boundR = routes[i][1]; answer++; }
        }
        answer++;

        return answer;
    }
}