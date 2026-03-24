import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	
	static int[] next = new int[1000001];
	static int[] prev = new int[1000001];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken()); // 이전 역 개수
		int M = Integer.parseInt(st.nextToken()); // 공사 횟수
	
		int j;
		
		int[] input = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < N; i++) input[i] = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < N; i++) {
			next[input[i]] = input[(i + 1) % N];
			prev[input[i]] = input[(i - 1 + N) % N];
		}
		
		for(int x = 0; x < M; x++) {
			st = new StringTokenizer(br.readLine());
			String type = st.nextToken();
			int i = Integer.parseInt(st.nextToken());
			int targetNext, targetPrev;
			
			switch(type) {
				case "BN": // 현 노드와 다음 노드 사이에
					j = Integer.parseInt(st.nextToken());
					targetNext = next[i];
					sb.append(targetNext).append("\n");
					
					next[i] = j; prev[j] = i;
					next[j] = targetNext; prev[targetNext] = j;
					break;
				case "BP": // 현 노드와 이전 노드 사이에
					j = Integer.parseInt(st.nextToken());
					targetPrev = prev[i];
					sb.append(targetPrev).append("\n");
					
					next[targetPrev] = j; prev[j] = targetPrev;
					next[j] = i; prev[i] = j;
					
					break;
				case "CN": // 찾은 노드의 다음역을 폐쇄하고 고유 번호 출력
					targetNext = next[i];
					sb.append(targetNext).append("\n");
					
					int nextNext = next[targetNext];
					next[i] = nextNext; prev[nextNext] = i;
					break;
				case "CP": // 찾은 노드의 이전역을 폐쇄하고 고유 번호 출력
					targetPrev = prev[i];
					sb.append(targetPrev).append("\n");
					
					int prevPrev = prev[targetPrev];
					next[prevPrev] = i; prev[i] = prevPrev;
					break;
			}
		}
		System.out.print(sb);
	}
}