import sys
import stdio
import random
import stddraw
import picture as p
import pygame
pygame.init()
pygame.mixer.init()
score = 0
number_of_moves = 10
hmatches = []
vmatches = []
stddraw.setCanvasSize(1300,980)
stddraw.setFontSize(70)
stddraw.setXscale(0.0,8.999)
stddraw.setYscale(0.0,9.999)
pic1 = p.Picture("strawberry.png")
pic2 = p.Picture("lemon.png")
pic3 = p.Picture("orange.png")
pic4 = p.Picture("pear.png")
pic5 = p.Picture("grapes.png")
pic6 = p.Picture("watermelon.png")
pic7 = p.Picture("background.png")
pic8 = p.Picture("heart.png")
pic9 = p.Picture("star.png")
pic10 = p.Picture("win.png")
pic11 = p.Picture("lose.png")
v_combo1 = pygame.mixer.Sound('v_combo1.ogg')
v_combo2 = pygame.mixer.Sound('v_combo2.ogg')
v_combo3 = pygame.mixer.Sound('v_combo3.ogg')
v_combo4 = pygame.mixer.Sound('v_combo4.ogg')
v_combo5 = pygame.mixer.Sound('v_combo5.ogg')
win = pygame.mixer.Sound('win.ogg')
lose = pygame.mixer.Sound('lose.ogg')
bgm = pygame.mixer.Sound('bgm.ogg')
meow = pygame.mixer.Sound('meow.ogg')
switch = pygame.mixer.Sound('switch.ogg')
match = pygame.mixer.Sound('Saint.ogg')
stddraw.setFontFamily("WORDSOFLOVE")
stddraw.setPenColor(stddraw.MAGENTA)
x = False
end = False
combo = -1
level = 1
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channel3 = pygame.mixer.Channel(3)
def update_without_score():
	stddraw.setFontFamily("WORDSOFLOVE")
	stddraw.setFontSize(70)
	stddraw.picture(pic7,4.5,5)
	stddraw.setFontSize(70)
	for i in range(9):
		for j in range(9):
			if game[i][j] == "strawberry":
				stddraw.picture(pic1,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "lemon":
				stddraw.picture(pic2,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "orange":
				stddraw.picture(pic3,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "pear":
				stddraw.picture(pic4,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "grapes":
				stddraw.picture(pic5,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "watermelon":
				stddraw.picture(pic6,(j + 1)*0.9,i+0.5)
	stddraw.text(1,9.5,":Score: ")
	stddraw.text(4.4,9.5,":Moves: ")
	stddraw.text(8,9.5,":Goal: ")
	
	stddraw.setFontFamily("Blah blah bang")
	stddraw.setFontSize(40)
	stddraw.text(8.7,9.5,"700")
	stddraw.text(5.3,9.5,str(number_of_moves))
def update():
	stddraw.setFontFamily("WORDSOFLOVE")
	stddraw.setFontSize(70)
	stddraw.picture(pic7,4.5,5)
	stddraw.setFontSize(70)
	for i in range(9):
		for j in range(9):
			if game[i][j] == "strawberry":
				stddraw.picture(pic1,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "lemon":
				stddraw.picture(pic2,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "orange":
				stddraw.picture(pic3,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "pear":
				stddraw.picture(pic4,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "grapes":
				stddraw.picture(pic5,(j + 1)*0.9,i+0.5)
			elif game[i][j] == "watermelon":
				stddraw.picture(pic6,(j + 1)*0.9,i+0.5)
	stddraw.text(1,9.5,":Score: ")
	stddraw.text(4.4,9.5,":Moves: ")
	stddraw.text(8,9.5,":Goal: ")
	stddraw.setFontFamily("Blah blah bang")
	stddraw.setFontSize(40)
	stddraw.text(8.7,9.5,"700")
	stddraw.text(1.8,9.5,str(score))
	stddraw.text(5.3,9.5,str(number_of_moves))
	if x:
		stddraw.show(0.0)

def find_match():
	
	hmatches= []
	vmatches = []
	matches = 0
	global score
	global combo
	temp_score = score
	for i in range (9):
		for j in range(8):
			if game[i][j] == game[i][j+1] != "null":
				matches += 1
				if matches == 2:
					hmatches.append(i)
					hmatches.append(j-1)
				if j == 7 and matches >= 2:
					hmatches.append(matches+1)
					
			elif matches >= 2:
					hmatches.append(matches+1)
					matches = 0
			elif matches < 2:
				matches = 0
		matches = 0
	
	matches = 0

					
	for i in range (9):
		for j in range(8):
			if game[j][i] == game[j + 1][i] != "null":
				matches += 1
				if matches == 2:
					vmatches.append(j-1)
					vmatches.append(i)
				if j == 7 and matches >= 2:
					vmatches.append(matches+1)
			elif matches >= 2:
					vmatches.append(matches+1)
					matches = 0
			elif matches < 2:
				matches = 0
		matches = 0
		
	if len(hmatches) > 0:
		for i in range (1,(len(hmatches)//3)+1):
			if hmatches[(i*3)-1] > 2:
				for j in range (hmatches[(i*3)-1]):
					if x:
						stddraw.show(60)
					game[hmatches[i*3-3]][hmatches[i*3-2] + j] = "null"
					score += 10*(combo+2)
				combo += 1
			y_s = (hmatches[i*3-3] +0.5)
			x_s = (hmatches[i*3-2]+1)*0.9+1
			delta_y = 9.5 - y_s
			delta_x = x_s - 1
			if x:
				channel2.play(match)
			while y_s < 9 and x:
				x_s -= (delta_x/10)
				y_s += (delta_y/10)
				
				stddraw.clear()
				stddraw.text(1.8,9.5,str(temp_score))
				update_without_score()
				stddraw.text(1.8,9.5,str(temp_score))
				stddraw.picture(pic9,x_s,y_s)
				stddraw.show(0)
			temp_score = score
	temp_score = score		
	if len(vmatches) > 0:
		for i in range (1,(len(vmatches)//3)+1):
			for j in range (vmatches[(i*3)-1]):
				if x:
					stddraw.show(60)
				game[vmatches[i*3-3]+j][vmatches[i*3-2]] = "null"
				score+=10*(combo+2)
			combo +=1
			y_s = (vmatches[i*3-3] +1.5)
			x_s = (vmatches[i*3-2]+1)*0.9
			delta_y = 9.5 - y_s
			delta_x = x_s - 1
			if x:
				channel2.play(match)
			while y_s < 9 and x:
				x_s -= (delta_x/10)
				y_s += (delta_y/10)
				
				stddraw.clear()
				stddraw.text(1.8,9.5,str(temp_score))
				update_without_score()
				stddraw.text(1.8,9.5,str(temp_score))
				stddraw.picture(pic9,x_s,y_s)
				stddraw.show(0)
			temp_score = score

	stddraw.clear()
	update()
	
	
	if x:
		stddraw.show(5)
		
	if len(hmatches) > 0 or len(vmatches) > 0 :
		return True
	else:
		return False
	

def fall():
	m = 1
	while m == 1:
		m = 0
		for i in range(1,9):
			for j in range (9):
				if game[8][j] == "null":
					game[8][j] = blocks[random.randrange(0,6)]
				if game[i][j] != "null" and game[i-1][j] == "null":
					a =	game[i][j]
					b = game[i-1][j]
					game[i][j] = b
					game[i-1][j] = a
					m = 1
					
					
				stddraw.clear()
			update()
			if x:
				stddraw.show(2)
				
	update()
	
	for i in range (9):
		for j in range(9):
			if game[i][j] == "null":
				game[i][j] = blocks[random.randrange(0,6)]
	
	

def swap(mx1,mx2,my1,my2):
	a = game[my1][mx1]
	b = game[my2][mx2]
	game[my1][mx1] = b
	game[my2][mx2] = a
	stddraw.clear()
	update()
def swap_valid(mx1,mx2,my1,my2):
	k = 0
	global number_of_moves
	if find_match():
		number_of_moves -=1
		update()
		find_match()
		if combo == 1 and x:
			channel3.play(v_combo1)
		elif combo == 2 and x:
			channel3.play(v_combo2)
		elif combo == 3 and x:
			channel3.play(v_combo3)
		elif combo == 4 and x:
			channel3.play(v_combo4)
		elif combo == 5 and x:
			channel3.play(v_combo5)
		fall()
		k = 1
		
		stddraw.show(0.0)
	while find_match():
		find_match()
		if combo == 1 and x:
			channel3.play(v_combo1)
		elif combo == 2 and x:
			channel3.play(v_combo2)
		elif combo == 3 and x:
			channel3.play(v_combo3)
		elif combo == 4 and x:
			channel3.play(v_combo4)
		elif combo == 5 and x:
			channel3.play(v_combo5)
		fall()
		k = 1
	if k == 0:
		channel2.play(switch)
		swap(mx1,mx2,my1,my2)
		

		
		
def no_more_moves():
	global end
	end = True
	for i in range (9):
		for j in range(9):
			if j+1 < 9 and game[i][j] == game[i][j+1]:
				if  j-2>-1 and game [i][j-2] == game[i][j]:
					end = False
				elif j+3<9 and game [i][j+3] == game[i][j]:
					end = False
				elif i+1<9 and j-1>-1 and game[i+1][j-1] == game[i][j]:
					end = False
				elif i-1<-1 and j-1>-1 and game[i-1][j-1] == game[i][j]:
					end = False
				elif i+1<9 and j+1>9 and game[i+1][j+1] == game[i][j]:
					end = False
				elif i-1<-1 and j+1>9 and game[i-1][j+1] == game[i][j]:
					end = False
			if j+2<9 and game[i][j] == game[i][j+2]:
				if i+1 < 9 and j+1 < 9 and game [i+1][j+1] == game[i][j]:
					end = False
				elif j+1<9 and i-1 >-1 and game [i-1][j+1] == game[i][j]:
					end = False
	
	for i in range (9):
		for j in range(9):
			if j+1 < 9 and game[j][i] == game[j+1][i]:
				if  j-2>-1 and game [j-2][i] == game[j][i]:
					end = False
				elif j+3<9 and game [j+3][i] == game[j][i]:
					end = False
				elif i+1<9 and j-1>-1 and game[j-1][i+1] == game[j][i]:
					end = False
				elif i-1<-1 and j-1>-1 and game[j-1][i-1] == game[j][i]:
					end = False
				elif j+1<9 and i+1>9 and game[j+1][i+1] == game[j][i]:
					end = False
				elif i-1<-1 and j+1>9 and game[i-1][j+1] == game[j][i]:
					end = False
			if j+2<9 and game[i][j] == game[j+2][i]:
				if i+1 < 9 and j+1 < 9 and game [i+1][j+1] == game[j][i]:
					end = False
				elif j+1<9 and i-1 >-1 and game [j+1][i-1] == game[i][j]:
					end = False
				
			
			
			
game = [[],[],[],[],[],[],[],[],[]]
blocks= ["strawberry","watermelon","pear","orange","lemon","grapes"]
for i in range (9):
	for j in range(9):
		game[i].append(blocks[random.randrange(0,6)])
update()
found = True
while find_match():
	find_match()
	fall()
x = True
score = 0
update()
no_more_moves()
first_click = True
second_click = True
channel1.play(bgm, loops = -1)
mx1 = 0
my1= 0
my2= 0
mx2 = 0
while end == False and score < 700 and number_of_moves > 0:
	combo = -1
	stddraw.show(0.0)
	while first_click:
		stddraw.show(0.0)
		if stddraw.mousePressed() and stddraw.mouseY() < 9 and stddraw.mouseX() > 0.5 and stddraw.mouseX() < 8.5:
			channel0.play(meow)
			if stddraw.mouseX()<1.4:
				mx1 = 0
			elif stddraw.mouseX()<2.289:
				mx1 = 1
			elif stddraw.mouseX()<3.17777:
				mx1 = 2
			elif stddraw.mouseX()<4.0666:
				mx1 = 3
			elif stddraw.mouseX()<4.9555:
				mx1 = 4
			elif stddraw.mouseX()<5.8444:
				mx1 = 5
			elif stddraw.mouseX()<6.7333:
				mx1 = 6
			elif stddraw.mouseX()< 7.6222:
				mx1 = 7
			else:
				mx1 = 8
			my1 = int(stddraw.mouseY())
			stddraw.setPenColor(stddraw.RED)
			stddraw.picture(pic8,(mx1+1.01)*0.9,my1-0.02+0.5)
			stddraw.setPenColor(stddraw.MAGENTA)
			first_click = False
			stddraw.show(0.0)
		
	while second_click:
		stddraw.show(0.0)
		if stddraw.mousePressed() and stddraw.mouseY() < 9:
			if stddraw.mouseX()<1.4:
				mx2 = 0
			elif stddraw.mouseX()<2.289:
				mx2 = 1
			elif stddraw.mouseX()<3.17777:
				mx2 = 2
			elif stddraw.mouseX()<4.0666:
				mx2 = 3
			elif stddraw.mouseX()<4.9555:
				mx2 = 4
			elif stddraw.mouseX()<5.8444:
				mx2 = 5
			elif stddraw.mouseX()<6.7333:
				mx2 = 6
			elif stddraw.mouseX()< 7.6222:
				mx2 = 7
			else:
				mx2 = 8
			my2 = int(stddraw.mouseY())
			
			if mx1 == mx2 + 1 and my1 == my2:
				channel2.play(switch)
				swap(mx1,mx2,my1,my2)
				swap_valid(mx1,mx2,my1,my2)	
			elif mx1 == mx2 - 1 and my1 == my2:
				channel2.play(switch)
				swap(mx1,mx2,my1,my2)
				swap_valid(mx1,mx2,my1,my2)
			elif mx1 == mx2 and my1 == my2 + 1:
				channel2.play(switch)
				swap(mx1,mx2,my1,my2)
				swap_valid(mx1,mx2,my1,my2)
			elif mx1 == mx2 and my1 == my2 - 1:
				channel2.play(switch)
				swap(mx1,mx2,my1,my2)
				swap_valid(mx1,mx2,my1,my2)
			else:
				second_click = False
				stddraw.clear()
				update()
			stddraw.show(0.0)
			second_click = False
	no_more_moves()
	first_click = True
	second_click = True
	

if score >= 700:
	stddraw.show(10)
	pygame.mixer.pause()
	channel1.play(win)
	stddraw.picture(pic10,4.5,5)
elif number_of_moves < 1:
	stddraw.show(10)
	pygame.mixer.pause()
	channel1.play(lose)
	stddraw.picture(pic11,4.5,5)
else:
	stddraw.setFontSize(200)
	stddraw.text(4.5,5,"No More Moves")
stddraw.show()