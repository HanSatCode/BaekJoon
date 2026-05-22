class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m]; dp[0][0] = 1;
        for(int[] c : puddles) dp[c[1] - 1][c[0] - 1] = -1;

        for(int i = 1; i < m; i++) { 
            if(dp[0][i - 1] <= 0) dp[0][i] = 0;
            else if (dp[0][i] != -1) dp[0][i] = 1;
        }
        for(int i = 1; i < n; i++) { 
            if(dp[i - 1][0] <= 0) dp[i][0] = 0;
            else if (dp[i][0] != -1) dp[i][0] = 1;
        }

        for(int y = 1; y < n; y++) {
            for(int x = 1; x < m; x++) {
                if (dp[y][x] == -1) { dp[y][x] = 0; continue; }

                int up  = (dp[y - 1][x] > 0) ? dp[y - 1][x] : 0;
                int left = (dp[y][x - 1] > 0) ? dp[y][x - 1] : 0;
                dp[y][x] = (up + left) % 1000000007;
            }
        }

        return dp[n - 1][m - 1];
    }
}