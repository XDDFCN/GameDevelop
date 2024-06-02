import tkinter
import time
import random

mainWindow = tkinter.Tk()
mainWindow.title("小仙鹤的弹球游戏")

gameCanvas = tkinter.Canvas(mainWindow, width=500, height=500)
gameCanvas.pack()

ovalID = gameCanvas.create_oval(30,40,10,20,fill="#FF5687",outline="orange",width=3)

while True:
    moveX = random.random()*80-40   #-40，40
    moveY = random.random()*80-40
    ballCoord = gameCanvas.coords(ovalID)
    if ballCoord[0]+moveX>=0 and ballCoord[1]+moveY<=500 and ballCoord[2]+moveX<=500 and ballCoord[3]+moveY>=0:
        gameCanvas.move(ovalID,moveX,moveY)
        mainWindow.update()
        time.sleep(0.1)   #小球每移动一下停留的秒数


# mainWindow.mainloop()   #可有可无，挑不出while True循环
