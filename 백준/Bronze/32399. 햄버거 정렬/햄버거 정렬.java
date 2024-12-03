import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arrayS = new String[3];
		String temp = br.readLine();
		
		int i = 0;
		int c = 0;
		
		//문자열 분리하기
		for(String s : temp.split("")) {
			if (! (s.equals(")") || s.equals("("))) {
				c = i;
			}
			arrayS[i] = s;
			i++;
		}
		
		//로직
		if(c == 1) {
			if(temp.equals("(" + arrayS[c] + ")")) System.out.println(0);
			else System.out.println(2);
		} else if (c == 0){
			if(temp.equals(arrayS[c] + ")(")) System.out.println(1);
			else System.out.println(1);
		} else { //c == 2
			System.out.println(1);
		}
	}
}