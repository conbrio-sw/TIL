package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class swea1954 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int i = 1; i <= T; i ++) {
			int N = Integer.parseInt(br.readLine());
			snail(N);
		}
	}
	public static void snail(int N) {
		int[][] mat = new int[N][N];
		int row_idx = 0;
		int col_idx = -1;
		int num = 1;
		int row_move = 0;
		int col_move = 1;
		while(true) {
			if(num > N*N) {
				break;
			}
			
			mat[row_idx+row_move][col_idx+col_move] = num;
			num++;
			row_idx += row_move;
			col_idx += col_move;
			if(row_idx==0 && col_idx == N-1) {
				row_move = 1;
				col_move = 0;
				continue;
			}
			if(row_idx==N-1 && col_idx==N-1) {
				row_move = 0;
				col_move = -1;
				continue;
			}
			if(row_idx==N-1&&col_idx == 0) {
				row_move = -1;
				col_move = 0;
				continue;
			}
			if(mat[row_idx+row_move][col_idx+col_move] != 0) {
				if(row_move == 1) {
					row_move = 0;
					col_move = -1;
				}
				else if(row_move == -1) {
					row_move = 0;
					col_move = 1;
				}
				else if(col_move == 1) {
					col_move = 0;
					row_move = 1;
				}
				else if(col_move == -1) {
					col_move = 0;
					row_move = -1;
				}
			}
			
		}
		for(int[] tempp : mat) {
			for(int temp : tempp) {
				System.out.print(temp + " ");
			}
			System.out.println();
		}
	}
}
