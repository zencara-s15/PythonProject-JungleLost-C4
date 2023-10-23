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
window.title('Group C4 - Juggle Game')
canvas = tk.Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, scrollregion=(0,0,3800,5000))
canvas.pack()
# Varaible
game_start = tk.PhotoImage(file="img/background/bg_game.png")
game_help = tk.PhotoImage(file="img/background/Group 5.png")
game_level = tk.PhotoImage(file="img/background/back_level.png")

btn_start_game = tk.PhotoImage(file="img/menu/start.png")
btn_exit_game = tk.PhotoImage(file="img/menu/exit.png")
btn_help_game = tk.PhotoImage(file="img/menu/help.png")
btn_back_game = tk.PhotoImage(file="img/menu/back.png")

level1 = tk.PhotoImage(file="img/menu/level1.png")
level2 = tk.PhotoImage(file="img/menu/level2.png")
level3 = tk.PhotoImage(file="img/menu/level3.png")

ground = tk.PhotoImage(file="img/robar.png")

# ________level2________

bg_level2=tk.PhotoImage(file="img/background/bgL2.png")

grass_level2 = tk.PhotoImage(file="img/grassl2.png")



# Show start game
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
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
    # canvas.create_image(500,400, image=bg_l1)

    canvas.create_image(140, 100, image=btn_back_game, tags="back")


def levelTwo(event):
    canvas.delete("all")
    canvas.create_image(600,350, image=bg_level2)
    canvas.create_image(1950,350, image=bg_level2)
    canvas.create_image(3300,350, image=bg_level2)
    #scrollbar
    scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

    canvas.create_image(300, 150, image=grass_level2)
    canvas.create_image(500, 350, image=grass_level2)
    canvas.create_image(700, 550, image=grass_level2)
    canvas.create_image(1100,550, image=grass_level2)
    canvas.create_image(900, 350, image=grass_level2)
    canvas.create_image(750, 150, image=grass_level2)
    canvas.create_image(1200, 150, image=grass_level2)
    canvas.create_image(1400, 350, image=grass_level2)
    canvas.create_image(1600, 550, image=grass_level2)
    canvas.create_image(1600, 150, image=grass_level2)

    canvas.create_image(140, 100, image=btn_back_game, tags="back")

def levelThree(event):
    canvas.delete("all")

    canvas.create_image(140, 100, image=btn_back_game, tags="back")

# create image
canvas.create_image(680, 372, image=game_start)
canvas.create_image(630,280, image=btn_start_game, tags="startgame")
canvas.create_image(630,540,image=btn_help_game, tags="help")
canvas.create_image(630,410,image=btn_exit_game, tags="exit")


# Bind the button clicks to the corresponding functions
canvas.tag_bind("help", "<Button-1>", gameHelp)
canvas.tag_bind("exit", "<Button-1>", gameExit)
canvas.tag_bind("back", "<Button-1>", gameShow)
canvas.tag_bind("startgame", "<Button-1>",levelGame )

canvas.tag_bind("level1", "<Button-1>", levelOne)
canvas.tag_bind("level2", "<Button-1>", levelTwo)
canvas.tag_bind("level3", "<Button-1>", levelThree)


canvas.pack(expand=True, fill='both')
window.mainloop()