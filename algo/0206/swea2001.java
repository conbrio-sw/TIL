package algo;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea2001 {
	public static void main(String[] args) throws IOException{
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int i = 1; i <= T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int [][] mat = new int[N][N];
			for(int j = 0; j < N; j++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int k =0; k < N; k++) {
					mat[j][k] = Integer.parseInt(st.nextToken());
				}	
			}
			System.out.println("#" + i + " " + killfly(mat, N, M));
		}

	}
	
	public static int killfly(int[][] mat, int N, int M) {
		int rst = 0;
		int [][] dp = new int[15][15];
		for(int i = 0; i < M; i++)
			for(int j = 0; j <M; j++)
				dp[0][0] += mat[i][j];
		for(int i = 0; i < N-M+1; i++) {
			for(int j = 0; j < N-M+1; j++) {
				if(i==0 && j==0)
					continue;
				if(j==0) {
					dp[i][j] = dp[i-1][j];
					for(int b = 0; b < M; b++) {
						dp[i][j] -= mat[i-1][j+b];
						dp[i][j] += mat[i-1+M][j+b];
					}
				}
				else {
					dp[i][j] = dp[i][j-1];
					for(int a = 0; a < M; a++) {
						dp[i][j] -= mat[i+a][j-1];
						dp[i][j] += mat[i+a][j-1+M];					
					}
				}
			}
		}
		for(int[] tempp : dp) {
			for(int temp : tempp) {
				if(temp > rst) {
					rst = temp;
				}
			}
		}
		return rst;
	}
	
	
}
