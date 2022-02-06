package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea1289 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 1; i <= T; i++) {
			String s = br.readLine();
			System.out.println("#"+ i + " " + solution(s));
		}

	}
	public static int solution(String s) {
		
		char temp = '0';
		char[] arr = s.toCharArray();
		int rst = 0;
		for(char chr : arr) {
			if(chr != temp) {
				rst += 1;
				if(temp == '0')
					temp = '1';
				else
					temp = '0';
			}
		}
		return rst;
		
	}
}
