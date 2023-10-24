import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk

# ---------------------------------------------------------------------------
# #=> CONSTANT
# ---------------------------------------------------------------------------

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
window.title('Group C5 - Juggle Game')
canvas = tk.Canvas(window)

# Varaible
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
btn_back_game = tk.PhotoImage(file="img/menu/come_back.png")
btn_restart_game = tk.PhotoImage(file="img/menu/restart.png")
btn_next_game = tk.PhotoImage(file="img/menu/next.png")


# ---------------------levelGame--------------------------

level1 = tk.PhotoImage(file="img/menu/level1.png")
level2 = tk.PhotoImage(file="img/menu/level2.png")
level3 = tk.PhotoImage(file="img/menu/level3.png")

# -------------------------------------------------------------------------
# ----------------------funtions-------------------------------------------
# -------------------------------------------------------------------------

# Show start game
def gameShow(event):
    canvas.delete("all")
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

# level game play
def levelOne(event):
    canvas.delete("all")
    canvas.create_image(140, 100, image=btn_back_game, tags="back")



def levelTwo(event):
    canvas.delete("all")
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

def levelThree(event):
    canvas.delete("all")
    canvas.create_image(140, 100, image=btn_back_game, tags="back")

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