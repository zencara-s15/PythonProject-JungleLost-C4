import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk
import time

# player ----
GRAVITY_FORCE = 10
JUMP_FORCE = 25
SPEED = 10
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
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, scrollregion=(0,0,3800,5000))
canvas.pack()
# Varaible
game_start = tk.PhotoImage(file="img/background/bg_game.png")
game_help = tk.PhotoImage(file="img/background/Game_help.png")
game_level = tk.PhotoImage(file="img/background/back_level.png")
# -----------------------back-ground--------------
game_start = tk.PhotoImage(file="img/background/bg_game.png")
game_help = tk.PhotoImage(file="img/background/Game_help.png")
game_level = tk.PhotoImage(file="img/background/back_level.png")
game_win = tk.PhotoImage(file="img/background/wingame.png")
game_lose = tk.PhotoImage(file="img/background/losegame.png")
game_i = tk.PhotoImage(file="img/menu/back.png")

# ----------------------buttons-----------------------

btn_start_game = tk.PhotoImage(file="img/menu/start.png")
btn_exit_game = tk.PhotoImage(file="img/menu/exit.png")
btn_help_game = tk.PhotoImage(file="img/menu/help.png")
btn_back_game = tk.PhotoImage(file="img/menu/back.png")
btn_back_game = tk.PhotoImage(file="img/menu/come_back.png")
btn_restart_game = tk.PhotoImage(file="img/menu/restart.png")
btn_next_game = tk.PhotoImage(file="img/menu/next.png")


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

bg_level2=tk.PhotoImage(file="img/background/bgL2.png")

bg_lvl3 = tk.PhotoImage(file="img/background/bgl3.png")
# ---------------- this place for create platform image for all lvl
grass_level2 = tk.PhotoImage(file="img/grassl2.png")

grass_lvl3_file=Image.open("img/menu/grassL3.png")
grass_lvl3_size =grass_lvl3_file.resize((200,50))
grass_lvl3 =ImageTk.PhotoImage(grass_lvl3_size)

plaform_file = Image.open("bg.jpg")  #this is for condition test only
plaform = ImageTk.PhotoImage(plaform_file)
# ---------------- this place for create enemies image for all lvl

rock_lvl2_file = Image.open("img/menu/rock-stones.webp")
rock_lvl2_size = rock_lvl2_file.resize((80,50))
rock_lvl2 = ImageTk.PhotoImage(rock_lvl2_size)

tiger_lvl2_file = Image.open("img/enemies/tiger.png")
tiger_lvl2_size =tiger_lvl2_file.resize((80,80))
tigerlvl2 = ImageTk.PhotoImage(tiger_lvl2_size)

snak_lvl2_file =Image.open("img/enemies/snak.png")
snak_lvl2_size = snak_lvl2_file.resize((50,50))
snak_lvl2 =ImageTk.PhotoImage(snak_lvl2_size)

trap_lvl2_file = Image.open("img/enemies/trap.webp")
trap_lvl2_size = trap_lvl2_file.resize((50,50))
trap_lvl2 = ImageTk.PhotoImage(trap_lvl2_size)

# ---------------- this place for create fruits image for all lvl
apple_level2_file = Image.open("img/enemies/apple.png")
apple_level2_size = apple_level2_file.resize((50,50))
apple_leveL2 =ImageTk.PhotoImage(apple_level2_size)


#-------------------this place for creat key img all lvl
key_lvl2_file= Image.open("img/key.png")
key_lvl2_size= key_lvl2_file.resize((50,25))
key_lvl2 =ImageTk.PhotoImage(key_lvl2_size)

# show start game
def gameShow(event):
    # canvas.delete("all")
    canvas.create_image(680, 350, image=game_start)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,540,image=btn_help_game, tags="help")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")

# show level game
def levelGame(event):
    canvas.delete(all)
    canvas.create_image(680,372, image=game_level)
    canvas.create_image(330,372, image=level1, tags="level1")
    canvas.create_image(630,372, image=level2, tags="level2")
    canvas.create_image(930,372, image=level3, tags="level3")
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

# show for how to play
def gameHelp(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

# close game
def gameExit(event):
    window.destroy()

# --------------------------win----------------------------
def winOne(event):
    canvas.delete("all")
    canvas.create_image(590,300, image=game_win)
    canvas.create_image(430,550, image=btn_back_game, tags="back")

    canvas.create_image(630,550, image=btn_restart_game, tags="restartOne")
    canvas.create_image(830,550, image=btn_next_game, tags="nextTwo")
  
def winTwo(event):
    canvas.delete("all")
    canvas.create_image(590,300, image=game_win)
    canvas.create_image(430,550, image=btn_back_game, tags="back")

    canvas.create_image(630,550, image=btn_restart_game, tags="restartTwo")
    canvas.create_image(830,550, image=btn_next_game, tags="nextThree")    
    
def winThree(event):
    canvas.delete("all")
    canvas.create_image(590,300, image=game_win)
    canvas.create_image(430,550, image=btn_back_game, tags="back") 
    canvas.create_image(630,550, image=btn_restart_game, tags="restartThree")

# -------------------------lose---------------------

def loseOne(event):
    canvas.delete("all")
    canvas.create_image(650,361,image=game_lose)
    canvas.create_image(750,550, image=btn_restart_game, tags="restartOne")

def loseTwo(event):
    canvas.delete("all")
    canvas.create_image(650,361,image=game_lose)
    canvas.create_image(750,550, image=btn_restart_game, tags="restartTwo")

def lsoeThree(event):
    canvas.delete("all")
    canvas.create_image(650,361,image=game_lose)
    canvas.create_image(750,550, image=btn_restart_game, tags="restartThree")


# create image start
def levelOne(event):
    canvas.delete("all") 
    global player
    canvas.create_image(700,350,image=bg)
    player = canvas.create_image(50, 100, image=play)
    canvas.create_rectangle(0,700,2800,700,fill="black",tags="GROUND")
    
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

def levelTwo(event):
    canvas.delete("all")
    canvas.delete("all")
    global player
    canvas.create_image(600,280, image=bg_level2)
    canvas.create_image(1950,280, image=bg_level2)
    canvas.create_image(3300,280, image=bg_level2)
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
    #______________________apple_level2______________,tags="GROUND"___
    canvas.create_image(300,110, image =apple_leveL2,tags= "FRUITS")
    canvas.create_image(900,280, image =apple_leveL2,tags= "FRUITS")
    canvas.create_image(1600,110, image =apple_leveL2,tags= "FRUITS")
    canvas.create_image(2200,280, image =apple_leveL2,tags= "FRUITS")
    canvas.create_image(2800,110, image =apple_leveL2,tags= "FRUITS")
    canvas.create_image(3600,110, image =apple_leveL2,tags= "FRUITS")
    #_____________________creat rocklvl2_____________________
    canvas.create_image(350, 600, image =rock_lvl2, tags ="ROCK")
    canvas.create_image(1350, 600, image =rock_lvl2, tags ="ROCK")
    canvas.create_image(2600, 600, image =rock_lvl2, tags ="ROCK")
    canvas.create_image(3400, 900, image =rock_lvl2, tags ="ROCK")
    #__________________creat enemies_________
    #__tiger__
    canvas.create_image(750,465, image=tigerlvl2, tags = "TIGER")
    canvas.create_image(2450,465, image=tigerlvl2, tags = "TIGER")
    canvas.create_image(80,600, image=tigerlvl2, tags = "TIGER")
    canvas.create_image(3400,600, image=tigerlvl2, tags = "TIGER")
    #__snak__
    canvas.create_image(500,280, image = snak_lvl2, tags ="SNAK")
    canvas.create_image(1850,275, image = snak_lvl2, tags ="SNAK")
    canvas.create_image(3050,275, image = snak_lvl2, tags ="SNAK")
    #___trap__
    canvas.create_image(1200,130, image = trap_lvl2, tags ="TRAP")
    canvas.create_image(2400,130, image = trap_lvl2, tags ="TRAP")

    #__________________Creat Key when winning lvl2______________
    canvas.create_image(2950, 290, image= key_lvl2, tags="KEY") 

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
    # platform
    canvas.create_image(150, 150, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(100, 630, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(400, 450, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(700, 270, image=grass_lvl3, tags ="GROUND") 
    canvas.create_image(400, 150, image=grass_lvl3, tags ="GROUND") 
    # canvas.create_image(110, 500, image=grass_lvl3, tags ="GROUND") 

# create image

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
        if "Right" in keyPressed:
            canvas.itemconfigure(player,image=charR)
            x += SPEED
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

# -------------------restart-game---------------

canvas.tag_bind("restartOne", "<Button-1>",levelOne )
canvas.tag_bind("restartTwo", "<Button-1>",levelTwo )
canvas.tag_bind("restartThree", "<Button-1>",levelThree )

# ------------------next-game------------------------

canvas.tag_bind("nextTwo", "<Button-1>",levelTwo )
canvas.tag_bind("nextThree", "<Button-1>",levelThree )

# ----------------level-game------------------------

canvas.tag_bind("level1", "<Button-1>", levelOne)
canvas.tag_bind("level2", "<Button-1>", levelTwo)
canvas.tag_bind("level3", "<Button-1>", levelThree)


canvas.pack(expand=True, fill='both')
window.mainloop()