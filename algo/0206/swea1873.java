package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea1873 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int i = 1; i <= T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			//필드 생성
			char[][] mat = new char[H][W];
			for(int j = 0; j < H; j++) {
				String str = br.readLine();
				char[] temp = str.toCharArray();
				for(int k =0; k < W; k++) {
					mat[j][k] = temp[k];
				}
			}
			//명령 생성
			int N = Integer.parseInt(br.readLine());
			String s = br.readLine();
			char[] commands = s.toCharArray();
			System.out.print("#" + i + " ");
			tank(mat, commands, H, W);
		}

	}
	
	public static void tank(char[][] mat, char[] commands, int H, int W) {
		int row_index = -1;
		int col_index = -1;
		// 현재 탱크 위치 찾기
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				if(mat[i][j] == '^' || mat[i][j] == 'v' || mat[i][j] == '<' || mat[i][j] == '>') {
					row_index = i;
					col_index = j;
				}	
			}
		}
		// 명령들 실행
		for(char command : commands) {
			//명령어가 S일 경우
			System.out.println("현재 명령어 : " + command + "현재 좌표 : " + row_index + " " + col_index);
			if(command == 'S') {
				//포탄의 방향에 따라 명령이 달라짐
				if(mat[row_index][col_index] == '^') {
					// 슈팅지점 저장
					int shooting_idx = row_index;
					while(true) {
						// 슈팅지점이 0 이면 위로 더 못쏘기 때문에 break
						if(shooting_idx == 0)
							break;
						shooting_idx -= 1;
						// 벽 만나면 멈추기
						if(mat[shooting_idx][col_index] == '*' || mat[shooting_idx][col_index] == '#') {
							// 벽돌 벽이면 부수기
							if(mat[shooting_idx][col_index] == '*')
								mat[shooting_idx][col_index] ='.';
							break;
						}
					}
				}
				if(mat[row_index][col_index] == 'v') {
					int shooting_idx = row_index;
					while(true) {
						// 슈팅지점이 H-1 이면 위로 더 못쏘기 때문에 break
						if(shooting_idx == H-1)
							break;
						shooting_idx += 1;
						// 벽 만나면 멈추기
						if(mat[shooting_idx][col_index] == '*' || mat[shooting_idx][col_index] == '#') {
							// 벽돌 벽이면 부수기
							if(mat[shooting_idx][col_index] == '*')
								mat[shooting_idx][col_index] ='.';
							break;
						}
					}
				}
				if(mat[row_index][col_index] == '<') {
					int shooting_idx = col_index;
					while(true) {
						// 슈팅지점이 0 이면 위로 더 못쏘기 때문에 break
						if(shooting_idx == 0)
							break;
						shooting_idx -= 1;
						// 벽 만나면 멈추기
						if(mat[row_index][shooting_idx] == '*' || mat[row_index][shooting_idx] == '#') {
							// 벽돌 벽이면 부수기
							if(mat[row_index][shooting_idx] == '*')
								mat[row_index][shooting_idx] ='.';
							break;
						}
					}
				}
				if(mat[row_index][col_index] == '>') {
					int shooting_idx = col_index;
					while(true) {
						// 슈팅지점이 W-1 이면 위로 더 못쏘기 때문에 break
						if(shooting_idx == W-1)
							break;
						shooting_idx += 1;
						// 벽 만나면 멈추기
						if(mat[row_index][shooting_idx] == '*' || mat[row_index][shooting_idx] == '#') {
							// 벽돌 벽이면 부수기
							if(mat[row_index][shooting_idx] == '*')
								mat[row_index][shooting_idx] ='.';
							break;
						}
					}
				}
			}
			//명령어가 이동일 경우
			if(command == 'U') {
				mat[row_index][col_index] = '^';
				if(row_index != 0 && mat[row_index-1][col_index] == '.') {
					mat[row_index-1][col_index] = '^';
					mat[row_index][col_index] = '.';
					row_index -= 1;
				}
			}
			if(command == 'D') {
				mat[row_index][col_index] = 'v';
				if(row_index != H-1 && mat[row_index+1][col_index] == '.') {
					mat[row_index+1][col_index] = 'v';
					mat[row_index][col_index] = '.';
					row_index += 1;
				}
			}
			if(command == 'L') {
				mat[row_index][col_index] = '<';
				if(col_index != 0 && mat[row_index][col_index-1] == '.') {
					mat[row_index][col_index-1] = '<';
					mat[row_index][col_index] = '.';
					col_index -= 1;
				}
			}
			if(command == 'R') {
				mat[row_index][col_index] = '>';
				if(col_index != W-1 && mat[row_index][col_index+1] == '.') {
					mat[row_index][col_index+1] = '>';
					mat[row_index][col_index] = '.';
					col_index += 1;
				}
			}
			for(char[] tempp : mat) {
				for(char temp : tempp) {
					System.out.print(temp);
				}
				System.out.println();
			}
		}
		// 출력
		for(char[] tempp : mat) {
			for(char temp : tempp) {
				System.out.print(temp);
			}
			System.out.println();
		}
	}

}
