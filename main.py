import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk
import time

# player ----
GRAVITY_FORCE = 10
JUMP_FORCE = 35
SPEED = 4
BG_SPEED = 3
TIMED_LOOP = 5

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
btn_back_game = tk.PhotoImage(file="img/menu/back.png")
btn_back_game = tk.PhotoImage(file="img/menu/come_back.png")


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

play_file = Image.open("img/character/playerR.png")
play_size = play_file.resize((50, 50))
play = ImageTk.PhotoImage(play_size)

charR_file = Image.open("img/character/playerR.png")
charR_size = charR_file.resize((50, 50))
charR = ImageTk.PhotoImage(charR_size)

charL_file = Image.open("img/character/playerL.png")
charL_size = charL_file.resize((50, 50))
charL = ImageTk.PhotoImage(charL_size)
player = canvas.create_image(50, 650, image=play)

# ---------------- this place for create background image for all lvl

bg_file = Image.open("bg.jpg")
bg = ImageTk.PhotoImage(bg_file)

bg_lvl1=tk.PhotoImage(file="img/background/bgL1.png")

bg_lvl2=tk.PhotoImage(file="img/background/bgL2.png")

bg_lvl3 = tk.PhotoImage(file="img/background/bgl3.png")

# ---------------- this place for create platform image for all lvl

grass_level1 = tk.PhotoImage(file="img/levelOne_image/grass.png") 

grass_level2 = tk.PhotoImage(file="img/grassl2.png")




# ---------------- this place for create enemies image for all lvl


snake_level1 = tk.PhotoImage(file="img/levelOne_image/snake.png")

# key_lvl1_file =Image.open("img/levelOne_image/key.png")
# key_lvl1_size= key_lvl1_file.resize((50,25))
# key_lvl1 = ImageTk.PhotoImage(key_lvl1_size)


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

trap_lvl2_file = Image.open("img/enemies/trap.webp")
trap_lvl2_size = trap_lvl2_file.resize((50,50))
trap_lvl2 = ImageTk.PhotoImage(trap_lvl2_size)

rock_lvl2_file = Image.open("img/menu/rock-stones.webp")
rock_lvl2_size = rock_lvl2_file.resize((80,50))
rock_lvl2 = ImageTk.PhotoImage(rock_lvl2_size)



# ---------------- this place for create enemies image for all lvl
tiger_level1 = tk.PhotoImage(file="img/levelOne_image/tiger.png")
rock_level1 = tk.PhotoImage(file="img/enemies/rock.png")
lava_wall =  tk.PhotoImage(file="lava.png")

# ---------------- this place for create fruits image for all lvl
apple_level2_file = Image.open("img/fruits/apple.png")
apple_level2_size = apple_level2_file.resize((50,50))
apple_leveL2 =ImageTk.PhotoImage(apple_level2_size)


apple_level1 = tk.PhotoImage(file="img/fruits/apple.png")


# #-------------------this place for creat key img all lvl
# key_lvl2_file= Image.open("img/key.png")
# key_lvl2_size= key_lvl2_file.resize((50,25))
# key_lvl2 =ImageTk.PhotoImage(key_lvl2_size)


# show start game
def gameShow(event):
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(630,150, image=game_menu)
    canvas.create_image(630,280, image=btn_start_game, tags="startgame")
    canvas.create_image(630,540,image=btn_help_game, tags="help")
    canvas.create_image(630,410,image=btn_exit_game, tags="exit")

# show level game
def levelGame(event):
    canvas.delete(all)
    canvas.create_image(650,352, image=game_level)
    canvas.create_image(250,302, image=level1, tags="level1")
    canvas.create_image(640,302, image=level2, tags="level2")
    canvas.create_image(1030,302, image=level3, tags="level3")
    canvas.create_image(640, 502, image=btn_back_game, tags="back")

# show for how to play
def gameHelp(event):
    # canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

# close game
def gameExit(event):
    window.destroy()

# --------------------------Screen_Scrolling-----------------------------------------------
def scroll_screen_right():
    canvas.move('all',-BG_SPEED,0)
    if canvas.coords('all')[0]<-2000:
        canvas.coords('all',2000,0)

def scroll_screen_left():
    canvas.move('all',+BG_SPEED,0)



# -------------------------lose---------------------
# -----------------------------------PROCESS GAME-----------------------------------------------
winning_fruit = 0
def gameWin():
    winOne()

def gameOver():
    loseOne()

def winOne():
    canvas.create_image(590,300, image=game_win)
    canvas.create_image(620,550, image=btn_back_game, tags="back1") 

def loseOne():
    canvas.create_image(650,361,image=game_lose)
    canvas.create_image(640,550, image=btn_back_game, tags="back1")


def levelOne(event):
    global player
    canvas.delete("all")
    
    canvas.create_image(600,280, image=bg_lvl1)
    canvas.create_image(1950,280, image=bg_lvl1)
    canvas.create_image(3300,280, image=bg_lvl1)
    player = canvas.create_image(50, 100, image=play)
    # #scrollbar

    scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
    
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
    canvas.create_image(2500, 150, image=grass_level1, tags="GROUND")
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
    fruit_id= canvas.create_image(840,410, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(3000,160, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(1700,210, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(2300,410, image=apple_level1, tags="FRUITS")
   
    
# ----------------------------------------------------------------------------------

    global enemies_id
    # enemies_id =canvas.create_image(200,410, image=enemy, tags="ENEMIES")
    enemies_id =canvas.create_image(800,570, image=tiger_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(2700,550, image=tiger_level1, tags="ENEMIES")

    enemies_id =canvas.create_image(2010,265, image=snake_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(2900,315, image=snake_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(930,260, image=snake_level1, tags="ENEMIES")

    enemies_id =canvas.create_image(400,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(1000,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(1600,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(2000,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(3000,590, image=rock_level1, tags="ENEMIES")
    enemies_id =canvas.create_image(3500,590, image=rock_level1, tags="ENEMIES")

    enemies_id =canvas.create_image(0,350, image=lava_wall, tags="ENEMIES")

# ----------------------------------------------------------------------------------

    canvas.create_rectangle(0,650,3800,700,fill="White",tags="GROUND")
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

def levelTwo(event):
    global player
    canvas.delete("all")
    canvas.create_image(600,280, image=bg_lvl2)
    canvas.create_image(1950,280, image=bg_lvl2)
    canvas.create_image(3300,280, image=bg_lvl2)
    canvas.create_rectangle(0,630,3800,700,fill="white",tags="GROUND")
    player = canvas.create_image(50, 100, image=play)
    # #scrollbar

    scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

    #_______________wall____________________________
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
    
# ----------------------------------------------------------------------------------

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
# fiuits
    global fruit_id 
 
    fruit_id = canvas.create_image(300,110, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(900,280, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(1600,110, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(2200,280, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(2800,110, image =apple_leveL2,tags= "FRUITS")
    fruit_id = canvas.create_image(3600,110, image =apple_leveL2,tags= "FRUITS")


    #__________________Creat Key when winning lvl2______________
    # canvas.create_image(2950, 290, image= key_lvl2, tags="KEY") 

def levelThree(event):  
    canvas.delete("all")
    global player
    # canvas.create_image(700,350,image=bg)
    player = canvas.create_image(50, 100, image=play)
    canvas.create_rectangle(0,700,2800,700,fill="black",tags="GROUND")
    canvas.create_image(140, 100, image=btn_back_game, tags="back")
    #background L3
    canvas.create_image(600,300, image=bg_lvl3)
    canvas.create_image(1950,300, image=bg_lvl3)
    canvas.create_image(3300,300, image=bg_lvl3)
    #scrollbar
    scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

    global fruit_id 

    fruit_id=canvas.create_image(840,410, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(3000,160, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(1700,210, image=apple_level1, tags="FRUITS")
    fruit_id=canvas.create_image(2300,410, image=apple_level1, tags="FRUITS")

    # player 
    player = canvas.create_image(50, 100, image=play)
    canvas.create_rectangle(0,620,3800,700,fill="black",tags="GROUND")

    # back btn 
    canvas.create_image(140, 100, image=btn_back_game, tags="back")


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
# def enemies():
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
    if coord[0] + dx - 15 < 0 or coord[0] + play.width() + dx > 2800:
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
        coord = canvas.coords(fruit_id)
        canvas.delete(fruit_id)

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

canvas.tag_bind("back2", "<Button-1>", loseOne)
canvas.tag_bind("back1", "<Button-1>", levelGame)

canvas.pack(expand=True, fill='both')
window.mainloop()