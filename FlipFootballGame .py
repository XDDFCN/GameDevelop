import tkinter
import time
import random
import math

mainWindow = tkinter.Tk()
mainWindow.title("小仙鹤的弹球游戏")
mainWindow.resizable(0,0)
w1=mainWindow.winfo_screenwidth()   #获取屏幕宽
h1=mainWindow.winfo_screenheight()   #获取屏幕高
w2=500  #指定当前窗体宽
h2=500  #指定当前窗体高
mainWindow.geometry("%dx%d+%d+%d"%(w2,h2,(w1-w2)/2,(h1-h2)/2))   #设置窗体大小及居中


gameCanvas = tkinter.Canvas(mainWindow, width=500, height=500)
gameCanvas.pack()

ovalID = gameCanvas.create_oval(30,40,10,20,fill="#FF5687",outline="orange",width=3)
boardID = gameCanvas.create_rectangle(0,470,70,480,fill="black", outline="black",width=3)

# image_file = tkinter.PhotoImage(file=r'./FlipFootballGameIcon.gif')
# image = gameCanvas.create_image(0, 0, anchor='nw', image=image_file)


moveX = random.random() * 10 - 5  # -5，5
moveY = random.random() * 10 - 5

def moveLeft(event):
    print("Left")
    pass
def moveRight(event):
    print("Right")
    pass

mainWindow.bind("<Left>",moveLeft)
mainWindow.bind("<Right>",moveRight)

while True:
    ballCoord = gameCanvas.coords(ovalID)
    if ballCoord[0]+moveX>0 and ballCoord[1]+moveY>0 and ballCoord[2]+moveX<500 and ballCoord[3]+moveY<500:
        gameCanvas.move(ovalID,moveX,moveY)
        mainWindow.update()
        time.sleep(0.02)   #小球每移动一下停留的秒数
    elif ballCoord[0]+moveX<=0 or ballCoord[1]+moveY>=0 or ballCoord[2]+moveX>=500 or ballCoord[3]+moveY<=500:
        signX = math.copysign(1, random.random() - 0.5)
        signY = math.copysign(1, random.random() - 0.5)
        moveX = (random.random() * 4 + 4)*signX
        moveY = (random.random() * 4 + 4)*signY

# mainWindow.mainloop()   #可有可无，跳不出while True循环
