package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea2805 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int i = 1; i <= T; i ++) {
			int N = Integer.parseInt(br.readLine());
			int [][] mat = new int[N][N];
			for(int j = 0; j < N; j++) {
				String s = br.readLine();
				char[] temp = s.toCharArray();
				for(int k =0; k < N; k++) {
					mat[j][k] = temp[k] - '0';
				}
			}
			System.out.println("#" + i + " " + money(mat, N));
		}
		
	}
	public static int money(int[][] mat, int N) {
		int rst = 0;
		int left_idx = (int)((N-1)*(0.5));
		int right_idx = (int)((N-1)*(0.5));
		int sign = 1;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(left_idx <= j && j <= right_idx) {
					rst += mat[i][j];
				}
			}
			if(left_idx == 0) {
				sign = -1;
			}
			left_idx = left_idx - sign;
			right_idx = right_idx + sign;
		}
		
		
		
		return rst;
	}

}
