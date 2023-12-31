import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk
import winsound
import time

# player ----
GRAVITY_FORCE = 10
JUMP_FORCE = 35
SPEED = 4
BG_SPEED = 3
TIMED_LOOP = 5
totalScore = 0
# enemy-move -----

xMove = 5

# press ------------- 
keyPressed = []

# ---------------------------------------------------------------------------
# #=> CONSTANT
# ---------------------------------------------------------------------------

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
window.title('Group C4 - Juggle Game')
canvas = tk.Canvas(window)

canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, scrollregion=(0,0,3800,5000))
canvas.pack()
# Varaible
game_start = tk.PhotoImage(file="img/background/bg_game.png")
game_help = tk.PhotoImage(file="img/background/Game_help.png")
game_level = tk.PhotoImage(file="img/background/back_level.png")
# -----------------------back-ground--------------
game_start = tk.PhotoImage(file="img/background/bg_game.png")
game_help = tk.PhotoImage(file="img/background/Game_help.png")
game_level = tk.PhotoImage(file="img/background/bg-level-game.png")
game_win = tk.PhotoImage(file="img/background/wingame.png")
game_lose = tk.PhotoImage(file="img/background/losegame.png")
game_menu = tk.PhotoImage(file="img/menu-game.png")

# ----------------------buttons-----------------------

btn_start_game = tk.PhotoImage(file="img/menu/start.png")
btn_exit_game = tk.PhotoImage(file="img/menu/exit.png")
btn_help_game = tk.PhotoImage(file="img/menu/help.png")
btn_back_game = tk.PhotoImage(file="img/menu/come_back.png")
btn_levle_back_game = tk.PhotoImage(file="img/menu/come_back.png")


# ---------------------levelGame--------------------------

level1 = tk.PhotoImage(file="img/menu/level1.png")
level2 = tk.PhotoImage(file="img/menu/level2.png")
level3 = tk.PhotoImage(file="img/menu/level3.png")

ground = tk.PhotoImage(file="img/robar.png")
# -------------------------------------------------------------------------
# ----------------------funtions-------------------------------------------
# -------------------------------------------------------------------------


# Show start game
# CHARACTER test for all lvl

play_file = Image.open("img/character/player_right.png")
play_size = play_file.resize((50, 50))
play = ImageTk.PhotoImage(play_size)

charR_file = Image.open("img/character/player_right.png")
charR_size = charR_file.resize((50, 50))
charR = ImageTk.PhotoImage(charR_size)

charL_file = Image.open("img/character/player_left.png")
charL_size = charL_file.resize((50, 50))
charL = ImageTk.PhotoImage(charL_size)
player = canvas.create_image(50, 650, image=play)

# ---------------- this place for create background image for all lvl

bg_file = Image.open("bg.jpg")
bg = ImageTk.PhotoImage(bg_file)

bg_lvl1=tk.PhotoImage(file="img/background/bgL1.png")
tree_bg_file = Image.open("img/menu/tree.png")
tree_bg_size =tree_bg_file.resize((100,150))
tree_bg = ImageTk.PhotoImage(tree_bg_size)

tree2_bg_file = Image.open("img/menu/tree2.png")
tree2_bg_size =tree2_bg_file.resize((100, 150))
tree2_bg = ImageTk.PhotoImage(tree2_bg_size)



bg_lvl2=tk.PhotoImage(file="img/background/bgL2.png")

bg_lvl3 = tk.PhotoImage(file="img/background/bgl3.png")

# ---------------- this place for create platform image for all lvl

grass_level1 = tk.PhotoImage(file="img/levelOne_image/grass.png") 

grass_level2 = tk.PhotoImage(file="img/grassl2.png")



grass_lvl3_file=Image.open("img/menu/grassL3.png")
grass_lvl3_size =grass_lvl3_file.resize((200,50))
grass_lvl3 =ImageTk.PhotoImage(grass_lvl3_size)

# ---------------- this place for create enemies image for all lvl


snake_level1 = tk.PhotoImage(file="img/levelOne_image/snake.png")

# key_lvl1_file =Image.open("img/levelOne_image/key.png")
# key_lvl1_size= key_lvl1_file.resize((50,25))
# key_lvl1 = ImageTk.PhotoImage(key_lvl1_size)

lava_wall =  tk.PhotoImage(file="lava.png")

# lvl 2 
tiger_lvl2_file = Image.open("img/enemies/tiger.png")
tiger_lvl2_size =tiger_lvl2_file.resize((80,80))
tigerlvl2 = ImageTk.PhotoImage(tiger_lvl2_size)

enemies_file = Image.open("enemy.png")
enemies_size = enemies_file.resize((50,50))
enemy =ImageTk.PhotoImage(enemies_size)

snak_lvl2_file =Image.open("img/enemies/snak.png")
snak_lvl2_size = snak_lvl2_file.resize((50,50))
snak_lvl2 =ImageTk.PhotoImage(snak_lvl2_size)


snake_level3_file =Image.open("img/enemies/snak.png")
snake_level3_size = snake_level3_file.resize((50,50))
snake_level3 =ImageTk.PhotoImage(snake_level3_size)

tiger_level3_file = Image.open("img/enemies/tiger.png")
tiger_level3_size = tiger_level3_file.resize((95,95))
tiger_level3 =ImageTk.PhotoImage(tiger_level3_size)

trap_lvl2_file = Image.open("img/enemies/trap.webp")
trap_lvl2_size = trap_lvl2_file.resize((50,50))
trap_lvl2 = ImageTk.PhotoImage(trap_lvl2_size)

rock_lvl2_file = Image.open("img/menu/rock-stones.webp")
rock_lvl2_size = rock_lvl2_file.resize((80,50))
rock_lvl2 = ImageTk.PhotoImage(rock_lvl2_size)

bird_level2_file=Image.open("img/levelOne_image/bird.png")
bird_level2_size =bird_level2_file.resize((70,70))
bird_level2 =ImageTk.PhotoImage(bird_level2_size)

birds_level2_file=Image.open("img/levelOne_image/birds.png")
birds_level2_size =birds_level2_file.resize((80,80))
birds_level2 =ImageTk.PhotoImage(birds_level2_size)

flower_level2_file=Image.open("img/levelOne_image/flower.png")
flower_level2_size =flower_level2_file.resize((120,120))
flower_level2 =ImageTk.PhotoImage(flower_level2_size)

flowergrass_level2_file=Image.open("img/levelOne_image/flower-grass.png")
flowergrass_level2_size =flowergrass_level2_file.resize((120,120))
flowergrass_level2 =ImageTk.PhotoImage(flowergrass_level2_size)

# ---------------- this place for create enemies image for all lvl
tiger_level1 = tk.PhotoImage(file="img/levelOne_image/tiger.png")
rock_level1 = tk.PhotoImage(file="img/enemies/rock.png")
lava_wall =  tk.PhotoImage(file="lava.png")

# ---------------- this place for create fruits image for all lvl
apple_level1 = tk.PhotoImage(file="img/fruits/apple.png")

apple_level2_file = Image.open("img/fruits/apple.png")
apple_level2_size = apple_level2_file.resize((50,50))
apple_leveL2 =ImageTk.PhotoImage(apple_level2_size)



banana_level3_file = Image.open("img/fruits/banana.png")
banana_level3_size = banana_level3_file.resize((55,55))
banana_level3 =ImageTk.PhotoImage(banana_level3_size)

# #-------------------this place for creat key img all lvl
# key_lvl2_file= Image.open("img/key.png")
# key_lvl2_size= key_lvl2_file.resize((50,25))
# key_lvl2 =ImageTk.PhotoImage(key_lvl2_size)


# show start game
def gameShow(event):
    winsound.PlaySound("sounds/bg.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(630,150, image=game_menu)
    canvas.create_image(630,280, image=btn_start_game, tags="startgame")
    canvas.create_image(630,540,image=btn_help_game, tags="help")
    canvas.create_image(630,410,image=btn_exit_game, tags="exit")




    
# show level game
def levelGame(event):
    winsound.PlaySound("sounds/soun-level.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(650,352, image=game_level)
    canvas.create_image(250,302, image=level1, tags="level1")
    canvas.create_image(640,302, image=level2, tags="level2")
    canvas.create_image(1030,302, image=level3, tags="level3")
    canvas.create_image(640, 502, image=btn_back_game, tags="back")



# show for how to play
def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(140, 100, image=btn_back_game, tags="back")
    winsound.PlaySound("sounds/click.wav", winsound.SND_FILENAME)


# close game
def gameExit(event):
    window.destroy()
    winsound.PlaySound("sounds/click.wav", winsound.SND_FILENAME)


# --------------------------Screen_Scrolling-----------------------------------------------
def scroll_screen_right():
    if canvas.coords(player)[0] < SCREEN_WIDTH and canvas.coords(player)[0] > SCREEN_WIDTH / 2:
        
        canvas.move('all',-BG_SPEED,0)


def scroll_screen_left():
    if canvas.coords(player)[0] > 0 and canvas.coords(player)[0] < SCREEN_WIDTH / 2:
        
        canvas.move('all',+BG_SPEED,0)

# --------------------------win----------------------------
def gameWin():
    global totalScore
    winOne()
    winsound.PlaySound("sounds/win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    totalScore =0 
    canvas.itemconfig(displayTotalCash, text=totalScore)

def winOne():
    canvas.create_image(590,300, image=game_win)
    canvas.create_image(620,550, image=btn_back_game, tags="back1")
# -------------------------lose---------------------

def gameOver():
    winsound.PlaySound("sounds/over.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    global totalScore
    loseOne()
    totalScore =0 
    canvas.itemconfig(displayTotalCash, text=totalScore)
    
def loseOne():
    canvas.create_image(650,361,image=game_lose)
    canvas.create_image(640,550, image=btn_back_game, tags="back1")
    


def levelOne(event):
    
    global player, displayTotalCash,fruit_id
    canvas.delete("all")
    canvas.create_rectangle(0,600,10000,601,fill="red",tags="GROUND")

    # sound
    winsound.PlaySound("sounds/click.wav", winsound.SND_FILENAME)
    # background
    canvas.create_image(0,0, image=bg_lvl1,anchor=NW)
    canvas.create_image(SCREEN_WIDTH,0, image=bg_lvl1,anchor=NW)
    canvas.create_image(SCREEN_WIDTH*2,0, image=bg_lvl1,anchor=NW)
    canvas.create_image(-700,0, image=bg_lvl1,anchor=NW)
    # player 
    player = canvas.create_image(50, 100, image=play)
    # score 
    displayTotalCash = canvas.create_text(700, 50, text=totalScore, font=("serif", 18 ,'bold'), fill="black")
    
    
    #grass  
    canvas.create_image(100, 195, image=grass_level1, tags="GROUND")
    canvas.create_image(230, 420, image=grass_level1, tags="GROUND")
    canvas.create_image(700, 230, image=grass_level1, tags="GROUND")
    canvas.create_image(800, 450, image=grass_level1, tags="GROUND")
    canvas.create_image(500, 350, image=grass_level1, tags="GROUND")
    canvas.create_image(950, 295, image=grass_level1, tags="GROUND")
    canvas.create_image(1200, 450, image=grass_level1, tags="GROUND")
    canvas.create_image(1300, 200, image=grass_level1, tags="GROUND")
    canvas.create_image(1700, 250, image=grass_level1, tags="GROUND")
    canvas.create_image(1500, 400, image=grass_level1, tags="GROUND")
    canvas.create_image(1900, 500, image=grass_level1, tags="GROUND")
    canvas.create_image(2000, 300, image=grass_level1, tags="GROUND")
    canvas.create_image(2300, 450, image=grass_level1, tags="GROUND")
    canvas.create_image(2700, 150, image=grass_level1, tags="GROUND")
    canvas.create_image(2900, 350, image=grass_level1, tags="GROUND")
    canvas.create_image(2500, 300, image=grass_level1, tags="GROUND")
    canvas.create_image(3000, 200, image=grass_level1, tags="GROUND")
    canvas.create_image(3300, 400, image=grass_level1, tags="GROUND")
    canvas.create_image(3600, 250, image=grass_level1, tags="GROUND")
    canvas.create_image(3400, 500, image=grass_level1, tags="GROUND")
    

    # fiuits
   
    global fruit_id 
    fruit_id=canvas.create_image(840,410, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(3000,160, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(1700,210, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(2300,410, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(2300,410, image=apple_level1, tags="FRUITS")
    #Tree on background
    canvas.create_image(770, 370, image =tree_bg)
    canvas.create_image(1750, 160, image =tree_bg)
    canvas.create_image(2360, 365, image =tree_bg)
    canvas.create_image(3060, 115, image =tree_bg)
    canvas.create_image(370, 470, image =tree2_bg)
    canvas.create_image(1000, 470, image =tree2_bg)
    canvas.create_image(1700, 470, image =tree2_bg)
    canvas.create_image(2500, 470, image =tree2_bg)
    canvas.create_image(2580, 470, image =tree2_bg)
    canvas.create_image(3200, 470, image =tree2_bg)
    canvas.create_image(3600, 470, image =tree2_bg)
    canvas.create_image(3700, 470, image =tree2_bg)
    # flags winner
    # canvas.create_image(3650, 205, image =flags, tags="FLAGS")
# ----------------------------------------------------------------------------------

    global enemies_id
    enemies_id =canvas.create_image(2700,550, image=tiger_level1, tags="ENEMIES")

    enemies_id =canvas.create_image(2010,265, image=snake_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(2900,315, image=snake_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(940,260, image=snake_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(400,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(1600,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(3000,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(3500,590, image=rock_level1, tags="ENEMIES")

    # lava_wall
    enemies_id =canvas.create_image(-140,350, image=lava_wall, tags="ENEMIES")
    enemies_id =canvas.create_image(-360,350, image=lava_wall, tags="ENEMIES")
    enemies_id =canvas.create_image(4200,350, image=lava_wall, tags="ENEMIES")
    
# ----------------------------------------------------------------------------------


def levelTwo(event):
    global player,displayTotalCash
    canvas.delete("all")

    winsound.PlaySound("sounds/click.wav", winsound.SND_FILENAME)
    # canvas.create_image(700,350, image=bg_lvl2,anchor=NW)
    # canvas.create_image(2100,350, image=bg_lvl2,anchor=NW)
    canvas.create_rectangle(0,650,3800,700,fill="white",tags="GROUND")


    canvas.create_image(600,350, image=bg_lvl2)
    canvas.create_image(1950,350, image=bg_lvl2)
    canvas.create_image(3300,350, image=bg_lvl2)
    canvas.create_image(-700,0, image=bg_lvl2,anchor=NW)

    player = canvas.create_image(50, 100, image=play)
    # #scrollbar
    displayTotalCash = canvas.create_text(700, 50, text=totalScore, font=("serif", 18 ,'bold'), fill="black")

    canvas.create_image(300, 150, image=grass_level2,  tags="GROUND")
    canvas.create_image(100, 400, image=grass_level2,  tags="GROUND")
    canvas.create_image(500, 320, image=grass_level2,  tags="GROUND")
    canvas.create_image(700, 500, image=grass_level2,  tags="GROUND")
    canvas.create_image(1100,500, image=grass_level2,  tags="GROUND")
    canvas.create_image(900, 320, image=grass_level2,  tags="GROUND")
    canvas.create_image(750, 150, image=grass_level2,  tags="GROUND")
    canvas.create_image(1200, 150, image=grass_level2, tags="GROUND")
    canvas.create_image(1400, 320, image=grass_level2, tags="GROUND")
    canvas.create_image(1600, 500, image=grass_level2, tags="GROUND")
    canvas.create_image(2000, 500, image=grass_level2, tags="GROUND")
    canvas.create_image(1800, 320, image=grass_level2, tags="GROUND")
    canvas.create_image(1600, 150, image=grass_level2, tags="GROUND")
    canvas.create_image(2000, 150, image=grass_level2, tags="GROUND")
    canvas.create_image(2200, 320, image=grass_level2, tags="GROUND")
    canvas.create_image(2400, 500, image=grass_level2, tags="GROUND")
    canvas.create_image(2800, 500, image=grass_level2, tags="GROUND")
    canvas.create_image(2600, 320, image=grass_level2, tags="GROUND")
    canvas.create_image(2400, 150, image=grass_level2, tags="GROUND")
    canvas.create_image(2800, 150, image=grass_level2, tags="GROUND")
    canvas.create_image(3000, 320, image=grass_level2, tags="GROUND")
    canvas.create_image(3200, 500, image=grass_level2, tags="GROUND")
    canvas.create_image(3600, 500, image=grass_level2, tags="GROUND")
    canvas.create_image(3400, 320, image=grass_level2, tags="GROUND")
    canvas.create_image(3200, 150, image=grass_level2, tags="GROUND")
    canvas.create_image(3600, 150, image=grass_level2, tags="GROUND")
    
    canvas.create_image(350, 600, image =rock_lvl2, tags ="ENEMIES")
    canvas.create_image(1350, 600, image =rock_lvl2, tags ="ENEMIES")
    canvas.create_image(2600, 600, image =rock_lvl2, tags ="ENEMIES")
    canvas.create_image(3400, 900, image =rock_lvl2, tags ="ENEMIES")
    # bird
    canvas.create_image(100, 80, image=bird_level2)
    canvas.create_image(170, 100, image=bird_level2)
    canvas.create_image(130, 120, image=bird_level2)
    canvas.create_image(800, 90, image=bird_level2)
    canvas.create_image(1500, 50, image=bird_level2)
    canvas.create_image(2000, 90, image=bird_level2)
    canvas.create_image(2500, 80, image=bird_level2)
    canvas.create_image(2900, 60, image=bird_level2)
    canvas.create_image(3200, 50, image=bird_level2)
    canvas.create_image(3700, 300, image=bird_level2)
    canvas.create_image(1300, 60, image=birds_level2)
    canvas.create_image(2500, 60, image=birds_level2)
    canvas.create_image(3000, 60, image=birds_level2)
    canvas.create_image(3700, 65, image=birds_level2)
    # flower
    canvas.create_image(200,550, image=flower_level2)
    canvas.create_image(1000,590, image=flower_level2)
    canvas.create_image(1800,600, image=flower_level2)
    canvas.create_image(2500,590, image=flower_level2)
    canvas.create_image(3000,570, image=flower_level2)
    canvas.create_image(3700,585, image=flower_level2)

    canvas.create_image(900,590, image=flowergrass_level2)
    canvas.create_image(3600,585, image=flowergrass_level2)
    global enemies_id
    #__tiger__
    enemies_id =canvas.create_image(2450,465, image=tigerlvl2, tags = "ENEMIES")
    enemies_id =canvas.create_image(80,600, image=tigerlvl2, tags = "ENEMIES")
    enemies_id =canvas.create_image(750,465, image=tigerlvl2, tags = "ENEMIES")
    enemies_id =canvas.create_image(3400,600, image=tigerlvl2, tags = "ENEMIES")
    #__snak__
    enemies_id =canvas.create_image(500,280, image = snak_lvl2, tags ="ENEMIES")
    enemies_id =canvas.create_image(1850,275, image = snak_lvl2, tags ="ENEMIES")
    enemies_id = canvas.create_image(3050,275, image = snak_lvl2, tags ="ENEMIES")
    #___trap__
    enemies_id =canvas.create_image(1200,130, image = trap_lvl2, tags ="ENEMIES")
    enemies_id =canvas.create_image(2400,130, image = trap_lvl2, tags ="ENEMIES")
    #____ROCK__
    enemies_id =canvas.create_image(350, 600, image =rock_lvl2, tags ="ENEMIES")
    enemies_id =canvas.create_image(1350, 600, image =rock_lvl2, tags ="ENEMIES")
    enemies_id =canvas.create_image(2600, 600, image =rock_lvl2, tags ="ENEMIES")
    enemies_id =canvas.create_image(3400, 900, image =rock_lvl2, tags ="ENEMIES")
    
# ----------------------------------------------------------------------------------
    global fruit_id 
 
    fruit_id = canvas.create_image(300,110, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(900,280, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(1600,110, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(2200,280, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(2800,110, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(3600,110, image =apple_leveL2,tags= "FRUITS")

    enemies_id =canvas.create_image(-140,350, image=lava_wall, tags="ENEMIES")
    enemies_id =canvas.create_image(-360,350, image=lava_wall, tags="ENEMIES")
    enemies_id =canvas.create_image(4300,350, image=lava_wall, tags="ENEMIES")
    
# ----------------------------------------------------------------------------------
# fiuits
    # global fruit_id 
 
    # fruit_id = canvas.create_image(300,110, image =apple_leveL2,tags= "FRUITS")
    # fruit_id = canvas.create_image(900,280, image =apple_leveL2,tags= "FRUITS")
    # fruit_id = canvas.create_image(1600,110, image =apple_leveL2,tags= "FRUITS")
    # fruit_id = canvas.create_image(2200,280, image =apple_leveL2,tags= "FRUITS")
    # fruit_id = canvas.create_image(2800,110, image =apple_leveL2,tags= "FRUITS")
    # fruit_id = canvas.create_image(3600,110, image =apple_leveL2,tags= "FRUITS")

    #__________________Creat Key when winning lvl2______________
    # canvas.create_image(2950, 290, image= key_lvl2, tags="KEY") 

def levelThree(event):  
    global player,displayTotalCash

    canvas.delete("all")
    
    # canvas.create_image(700,350,image=bg)
    winsound.PlaySound("sounds/click.wav", winsound.SND_FILENAME)

    player = canvas.create_image(50, 100, image=play)
    canvas.create_rectangle(0,700,2800,700,fill="black",tags="GROUND")

    displayTotalCash = canvas.create_text(700, 50, text=totalScore, font=("serif", 18 ,'bold'), fill="black")

    # platform
    canvas.create_image(100, 200, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(100, 500, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(400, 340, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(590, 150, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(810, 340, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(1130, 500, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(1730, 500, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(1400, 340, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(1690, 150, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(1090, 150, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(2050, 340, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(2390, 150, image=grass_lvl3, tags ="GROUND")
    canvas.create_image(2430, 500, image=grass_lvl3, tags ="GROUND")
    canvas.create_image(2700, 340, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(3080, 500, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(3040, 150, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(3350, 340, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(3730, 500, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(3690, 150, image=grass_lvl3, tags ="GROUND") 

    global fruit_id 

    fruit_id=canvas.create_image(1100,465, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(600,115, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(50,460, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(810,310, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(3045,115, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(3075,460, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(1640,120, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(3730,120, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(2400,460, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(2050,310, image=banana_level3, tags="FRUITS")
    fruit_id=canvas.create_image(3700,470, image=banana_level3, tags="FRUITS")

    global enemies_id

    # tiger
    enemies_id =canvas.create_image(120,590, image=tiger_level3, tags="ENEMIES")
    enemies_id =canvas.create_image(2700,550, image=tiger_level3, tags="ENEMIES")
    enemies_id =canvas.create_image(1300,560, image=tiger_level3, tags="ENEMIES")
    enemies_id =canvas.create_image(3670,570, image=tiger_level3, tags="ENEMIES")
    # rock
    enemies_id =canvas.create_image(550,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(2500,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(3100,590, image=rock_level1, tags="ENEMIES")
    # snake
    enemies_id =canvas.create_image(150,460, image = snake_level3, tags ="ENEMIES")
    enemies_id =canvas.create_image(1700,460, image = snake_level3, tags ="ENEMIES")
    enemies_id =canvas.create_image(2450,130, image = snake_level3, tags ="ENEMIES")
    enemies_id = canvas.create_image(3650,110, image = snake_level3, tags ="ENEMIES")
    enemies_id = canvas.create_image(1760,120, image = snake_level3, tags ="ENEMIES")
    # flags winner
    # canvas.create_image(3650, 200, image =flags, tags="FLAGS")


# FUNCTION__________________eat fruits 
def eat_fruit():
    coord = canvas.coords(player)
    fruits = canvas.find_withtag("FRUITS")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + play.width(),coord[1] + play.height())
    for fr in fruits:
        if fr in overlap:
            return fr      
    return 0
    
# FUNCTION___________________ENEMIES​​ AND LOST CONDITIION
def meet_enemies():
    coord = canvas.coords(player)
    enemies = canvas.find_withtag("ENEMIES")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + play.width(),coord[1] + play.height())
    for en in enemies:
        if en in overlap:
            return en
    return 0
# ------------- gravity function and movement ---------------------
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    grounds = canvas.find_withtag("GROUND")
    if coord[0] + dx - 15 < 0 or coord[0] + play.width() + dx > SCREEN_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0] , coord[1], coord[0] + dx + 50, coord[1] + dy + 15)
    else:
        overlap = canvas.find_overlapping(coord[0] + dx, coord[1] + dy, coord[0] - play.width(), coord[1] - play.height())

    for ground in grounds:
        if ground in overlap:
            return False
        
    global fruit_id
    fruit_id = eat_fruit()
    if fruit_id > 0:
        global totalScore
        coord = canvas.coords(fruit_id)
        totalScore += 1
        canvas.itemconfig(displayTotalCash, text=totalScore)
        canvas.delete(fruit_id)
        winsound.PlaySound("sounds/eat.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
     
        if totalScore == 4:
            coord = canvas.coords(fruit_id)
            gameWin()
        return True

    global enemies_id
    enemies_id = meet_enemies()
    if enemies_id > 0:
        coord = canvas.coords(enemies_id)
        canvas.itemconfig(player,image=enemy)
        gameOver()
    return True


def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)
          
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            canvas.itemconfigure(player,image=charL)
            x -= SPEED
            scroll_screen_left()
        if "Right" in keyPressed:
            canvas.itemconfigure(player,image=charR)
            x += SPEED
            scroll_screen_right()
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
            winsound.PlaySound("sounds/jump.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

        if check_movement(x):
            canvas.move(player, x, 0)
        window.after(TIMED_LOOP, move)

def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

gravity()
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)


# ----------------------------------------------

# create image menu
canvas.create_image(680, 372, image=game_start)
canvas.create_image(630,150, image=game_menu)
canvas.create_image(630,280, image=btn_start_game, tags="startgame")
canvas.create_image(630,540,image=btn_help_game, tags="help")
canvas.create_image(630,410,image=btn_exit_game, tags="exit")
winsound.PlaySound("sounds/bg.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# ------------------------------------------------------------------------
# Bind the button clicks to the corresponding functions
# ------------------------------------------------------------------------

canvas.tag_bind("help", "<Button-1>", gameHelp)
canvas.tag_bind("exit", "<Button-1>", gameExit)
canvas.tag_bind("back", "<Button-1>", gameShow)
canvas.tag_bind("startgame", "<Button-1>",levelGame )

# ----------------level-game------------------------

canvas.tag_bind("level1", "<Button-1>", levelOne)
canvas.tag_bind("level2", "<Button-1>", levelTwo)
canvas.tag_bind("level3", "<Button-1>", levelThree)

canvas.tag_bind("back1", "<Button-1>", levelGame)

canvas.pack(expand=True, fill='both')
window.mainloop()