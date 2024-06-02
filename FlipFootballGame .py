import tkinter
import time
import random
import math

mainWindow = tkinter.Tk()
mainWindow.title("小仙鹤的弹球游戏")

gameCanvas = tkinter.Canvas(mainWindow, width=500, height=500)
gameCanvas.pack()

ovalID = gameCanvas.create_oval(30,40,10,20,fill="#FF5687",outline="orange",width=3)
board = gameCanvas.create_rectangle(0,470,60,480)

# image_file = tkinter.PhotoImage(file=r'./FlipFootballGameIcon.gif')
# image = gameCanvas.create_image(0, 0, anchor='nw', image=image_file)


moveX = random.random() * 10 - 5  # -5，5
moveY = random.random() * 10 - 5


while True:
    ballCoord = gameCanvas.coords(ovalID)
    if ballCoord[0]+moveX>0 and ballCoord[1]+moveY<500 and ballCoord[2]+moveX<500 and ballCoord[3]+moveY>0:
        gameCanvas.move(ovalID,moveX,moveY)
        mainWindow.update()
        time.sleep(0.02)   #小球每移动一下停留的秒数
    elif ballCoord[0]+moveX<=0 or ballCoord[1]+moveY>=500 or ballCoord[2]+moveX>=500 or ballCoord[3]+moveY<=0:
        signX = math.copysign(1, random.random() - 0.5)
        signY = math.copysign(1, random.random() - 0.5)
        moveX = (random.random() * 4 + 4)*signX
        moveY = (random.random() * 4 + 4)*signY

# mainWindow.mainloop()   #可有可无，跳不出while True循环
