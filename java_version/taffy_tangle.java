import java.util.ArrayList;
import java.util.List;
import java.util.Random;
public class taffy_tangle {
	static int y;
	static Boolean end;
	static int number_of_moves;
	public static void no_move_moves(String[][] game){
		end = true;
		for (int i=0;i<9;i++){
			for (int j=0;j<7;j++){
				if (j+1 < 7 && game[i][j] == game[i][j+1]){
					if  (j-2>-1 && game [i][j-2] == game[i][j]){
						end = false;
					}
					else if (j+3<7 && game [i][j+3] == game[i][j]){
						end = false;
					}
					else if (i+1<9 && j-1>-1 && game[i+1][j-1] == game[i][j]){
						end = false;
					}
					else if (i-1<-1 && j-1>-1 && game[i-1][j-1] == game[i][j]){
						end = false;
					}
					else if (i+1<9 && j+1>7 && game[i+1][j+1] == game[i][j]){
						end = false;
					}
					else if (i-1<-1 && j+1>7 && game[i-1][j+1] == game[i][j]){
						end = false;
					}
				}
				if (j+2<7 && game[i][j] == game[i][j+2]){
					if (i+1 < 9 && j+1 < 7 && game [i+1][j+1] == game[i][j]){
						end = false;
					}
					else if (j+1<7 && i-1 >-1 && game [i-1][j+1] == game[i][j]){
						end = false;
					}
				}
			}
		}
		for (int i=0;i<7;i++){
			for (int j=0;j<9;j++){
				if (j+1 < 9 && game[j][i] == game[j+1][i]){
					if  (j-2>-1 && game [j-2][i] == game[j][i]){
						end = false;
					}
					else if (j+3<9 && game [j+3][i] == game[j][i]){
						end = false;
					}
					else if (i+1<7 && j-1>-1 && game[j-1][i+1] == game[j][i]){
						end = false;
					}
					else if (i-1<-1 && j-1>-1 && game[j-1][i-1] == game[j][i]){
						end = false;
					}
					else if (j+1<9 && i+1>7 && game[j+1][i+1] == game[j][i]){
						end = false;
					}
					else if (i-1<-1 && j+1>7 && game[i-1][j+1] == game[j][i]){
						end = false;
					}
				}
				if (j+2<9 && game[i][j] == game[j+2][i]){
					if (i+1 < 9 && j+1 < 7 && game [i+1][j+1] == game[j][i]){
						end = false;
					}
					else if (j+1<9 && i-1 >-1 && game [j+1][i-1] == game[i][j]){
						end = false;
					}
				}
			}
		}
	}
	public static void update(Integer score, Boolean x, String[][] game){
		StdDraw.picture(3.5, 5, "background.png");
		for (int i=0;i<9;i++){
			for (int j=0;j<7;j++){
				if (game[i][j] == "strawberry"){
					StdDraw.picture(j+0.5,i+0.5,"strawberry.png");
				}
				else if (game[i][j] == "lemon"){
					StdDraw.picture(j+0.5,i+0.5,"lemon.png");
				}
				else if (game[i][j] == "orange"){
					StdDraw.picture(j+0.5,i+0.5,"orange.png");
				}
				else if (game[i][j] == "pear"){
					StdDraw.picture(j+0.5,i+0.5,"pear.png");
				}
				else if (game[i][j] == "grapes"){
					StdDraw.picture(j+0.5,i+0.5,"grapes.png");
				}
				else if (game[i][j] == "watermelon"){
					StdDraw.picture(j+0.5,i+0.5,"watermelon.png");
				}
			}
		}
		StdDraw.text(1,9.5,"Score: "+ Integer.toString(y));
		StdDraw.text(3,9.5,"Moves: "+ Integer.toString(number_of_moves));
		if (x){
			StdDraw.show();
		}
	}
	public static void swap(int mx1,int mx2,int my1,int my2,String[][]game,Integer score,Boolean x){
		String a = game[my1][mx1];
		String b = game[my2][mx2];
		game[my1][mx1] = b;
		game[my2][mx2] = a;
		StdDraw.clear();
		update(score,x,game);
	}
	public static boolean find_match(int score,List<Integer> vmatches,List<Integer> hmatches,String[][]game,Boolean x){
		hmatches.clear();
		vmatches.clear();
		int matches = 0;
		
		for (int i =0; i < 9;i++){
			for (int j =0; j < 6;j++){
				if (game[i][j] == game[i][j+1] && game[i][j] != "null"){
					matches += 1;
					if (matches == 2){
						hmatches.add(i);
						hmatches.add(j-1);
					}
						if (j == 5 && matches >= 2){
							
							hmatches.add(matches+1);
						}
					
				}		
				else if (matches >= 2){
							
							hmatches.add(matches+1);						
							matches = 0;
				}
				else if (matches < 2){
						matches = 0;
				}
			}matches = 0;
		}
			matches = 0;
			
			
				for (int i =0; i < 7;i++){
					for (int j =0; j < 8;j++){
						if (game[j][i] == game[j + 1][i] && game[j][i] != "null"){
							matches += 1;
							if (matches == 2){
								vmatches.add(j-1);
								vmatches.add(i);
							}
							if (j == 7 && matches >= 2){
								vmatches.add(matches+1);
							}
						}
						else if (matches >= 2){
								vmatches.add(matches+1);
								matches = 0;
						}
						else if (matches < 2){
							matches = 0;
						}
					}
				
					matches = 0;
				}
					
				if (hmatches.size() > 0){
					int size = hmatches.size();
					for (int i = 1;i <((int) size/3)+1;i++){
						if (hmatches.get((i*3)-1) > 2){
							for (int j = 0; j < hmatches.get((i*3)-1);j++){
								if (hmatches.get(i*3-2) + j < 7 && i*3-3 > -1){
								if (x){
									StdDraw.pause(80);
								}
								game[hmatches.get(i*3-3)][hmatches.get(i*3-2) + j] = "null";	
								score += 1;
								}
							}
						}
					}
				}
				if (vmatches.size() > 0){
					int size = vmatches.size();
					for (int i = 1;i <(size/3)+1;i++){
						for (int j = 0; j < vmatches.get((i*3)-1);j++){
							if (x){
								StdDraw.pause(80);
							}
							game[vmatches.get(i*3-3)+j][vmatches.get(i*3-2)] = "null";
							score+=1;
					}
				}
				}
				y += score;
				StdDraw.clear();
				update(score,x,game);
				if (x){
					StdDraw.pause(100);
				}
				if (hmatches.size() > 0 || vmatches.size() > 0) {
					return true;
				}
				else{
					return false;
				}

	}

	public static void fall(String[][] game,List<String> blocks,Integer score, Boolean x){
		int m = 1;
		while (m == 1){
			m = 0;
			for (int i = 1; i < 9; i++){
				for (int j = 0; j < 7; j++){
					if (game[8][j] == "null"){
						Random ran = new Random();
						int index = ran.nextInt(6);
						game[8][j] = blocks.get(index);
					}
					if (game[i][j] != "null" && game[i-1][j] == "null"){						
						String a = game[i][j];
						String b = game[i-1][j];
						game[i][j] = b;
						game[i-1][j] = a;
						m = 1;
					}
				}		
					StdDraw.clear();
			}
			update(score,x,game);
				if (x){
					StdDraw.pause(100);
				}
		}
		
		update(score,x,game);
				
		for (int i = 1; i < 9; i++){
			for (int j = 1; j < 7; j++){
				if (game[i][j] == "null"){
					Random ran = new Random();
					int index = ran.nextInt(6);
					game[i][j] = blocks.get(index);
				}
			}
		}
	}
	
	public static void swap_valid(int mx1,int mx2,int my1,int my2,String[][] game,Integer score,Boolean x,List<String> blocks,List<Integer> vmatches,List<Integer> hmatches){
		int k = 0;
		if (find_match(score,vmatches,hmatches,game,x)){
			number_of_moves -=1;
			find_match(score,vmatches,hmatches,game,x);
			fall(game,blocks,score,x);
			k = 1;
			
			update(score,x,game);
		}
		while (find_match(score,vmatches,hmatches,game,x)){
			find_match(score,vmatches,hmatches,game,x);
			fall(game,blocks,score,x);
			k = 1;
		}
			if (k == 0){
				swap(mx1,mx2,my1,my2,game,score,x);
			}
		
	}
	public static void main(String[] args) {
		StdDraw.enableDoubleBuffering();
		StdDraw.setXscale(0.0,6.999);
		StdDraw.setYscale(0.0,9.999);
		List<Integer> vmatches = new ArrayList<Integer>();
		List<Integer> hmatches = new ArrayList<Integer>();
		Boolean x = false;
		int score = 0;
		String[][] game = new String[9][];
		for (int i =0; i < 9;i++){
			game[i] = new String[7];

			}
		List<String> blocks = new ArrayList<String>();
		blocks.add("strawberry");
		blocks.add("grapes");
		blocks.add("pear");
		blocks.add("watermelon");
		blocks.add("lemon");
		blocks.add("orange");
		for (int i = 0; i <9;i++){
			for (int j = 0; j <7;j++){
				Random ran = new Random();
				int index = ran.nextInt(6);
				game[i][j] = blocks.get(index);
			}
		}
		number_of_moves = 10;
		update(score,x,game);
		while (find_match(score,vmatches,hmatches,game,x)){
			find_match(score,vmatches,hmatches,game,x);
			fall(game,blocks,score,x);
		}
		x = true;
		y = 0;
		update(score,x,game);
		no_move_moves(game);
		Boolean first_click = true;
		Boolean second_click = true;
	
		int mx1 = 0;
		int my1 = 0;
		int my2 = 0;
		int mx2 = 0;
		while (end == false && y < 50 && number_of_moves > 0){
			StdDraw.show();
			StdDraw.pause(200);
			while (first_click){
				StdDraw.pause(60);
				mx1 = 0;
				my1 = 0;
				mx2 = 0;
				my2 = 0;
				if (StdDraw.isMousePressed() && StdDraw.mouseY() < 9){
					mx1 = (int)StdDraw.mouseX();
					my1 = (int)StdDraw.mouseY();
					StdDraw.setPenColor(StdDraw.RED);
					StdDraw.square(mx1+0.5,my1+0.5,0.33);
					StdDraw.setPenColor(StdDraw.BLACK);
					first_click = false;
					StdDraw.show();
				}
			}
			StdDraw.pause(200);
			StdDraw.show();
			while (second_click){
				StdDraw.pause(60);
				if (StdDraw.isMousePressed()&& StdDraw.mouseY() < 9){
					mx2 = (int)StdDraw.mouseX();
					my2 = (int)StdDraw.mouseY();
					if (mx1 == mx2 + 1 && my1 == my2){
						swap(mx1,mx2,my1,my2,game,score,x);
						swap_valid(mx1,mx2,my1,my2,game,score,x,blocks,vmatches,hmatches);
					}
					else if( mx1 == mx2 - 1 && my1 == my2){
						swap(mx1,mx2,my1,my2,game,score,x);
						swap_valid(mx1,mx2,my1,my2,game,score,x,blocks,vmatches,hmatches);
					}
					else if (mx1 == mx2 && my1 == my2 + 1){
						swap(mx1,mx2,my1,my2,game,score,x);
						swap_valid(mx1,mx2,my1,my2,game,score,x,blocks,vmatches,hmatches);
					}
					else if (mx1 == mx2 && my1 == my2 - 1){
						swap(mx1,mx2,my1,my2,game,score,x);
						swap_valid(mx1,mx2,my1,my2,game,score,x,blocks,vmatches,hmatches);
					}
					else{
						StdDraw.clear();
						
						mx1 = 0;
						my1 = 0;
						my2 = 0;
						mx2 = 0;
						second_click = false;
						update(score,x,game);
						StdDraw.show();
					}
					
					second_click = false;
					StdDraw.show();
				}
			}
				no_move_moves(game);
				first_click = true;
				second_click = true;
				
		}
		if (y >= 50){
			StdDraw.text(6,9.5,"You win");
			}
		else if (number_of_moves <1){
			StdDraw.text(6,9.5,"You lose");
			}
		else{
				StdDraw.text(6,9.5,"No More Moves");
		}
		StdDraw.show();
		
	}

}
