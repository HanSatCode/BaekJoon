import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        
        int n = triangle.length;
        int[][] dp = new int[n][]; for(int i = 0; i < n; i++) { dp[i] = new int[i + 1]; }

        dp[0][0] = triangle[0][0];
        for(int i = 1; i < n; i++) {
            int preLastIndex = triangle[i - 1].length - 1;
            int curLastIndex = triangle[i].length - 1;
            dp[i][0] = dp[i - 1][0] + triangle[i][0];
            dp[i][curLastIndex] = dp[i - 1][preLastIndex] + triangle[i][curLastIndex];
        }

        for(int i = 2; i < n; i++) {
            for(int j = 1; j < triangle[i].length - 1; j++) {
                dp[i][j] = triangle[i][j] + Math.max(dp[i - 1][j - 1], dp[i - 1][j]);
            }
        }

        answer = Arrays.stream(dp[n - 1]).max().getAsInt();
        return answer;
    }
}