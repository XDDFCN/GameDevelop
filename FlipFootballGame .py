import tkinter
import time
import random
import math
import tkinter.messagebox

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
boardID = gameCanvas.create_rectangle(0,470,100,480,fill="black", outline="black",width=3)

# image_file = tkinter.PhotoImage(file=r'./FlipFootballGameIcon.gif')
# image = gameCanvas.create_image(0, 0, anchor='nw', image=image_file)


scoreLabel = tkinter.Label(mainWindow, text="得分：")
scoreLabel.place(x=400,y=10)
varLabel = tkinter.Label(mainWindow, text=" ")
varLabel.place(x=435,y=10)

moveXBall = random.random() * 10 - 5  # -5，5
moveYBall = random.random() * 10 - 5

# def Scoring_rule(message):
#     varLabel.config(message)


class Board:
    moveXBoard = 0
    def moveLeft(self,event):
        self.moveXBoard = -8
    def moveRight(self,event):
        self.moveXBoard = 8
board = Board()

mainWindow.bind("<Left>",board.moveLeft)
mainWindow.bind("<Right>",board.moveRight)

realtimeScore = 0


while True:
    boardCoord = gameCanvas.coords(boardID)
    if boardCoord[0]+board.moveXBoard>=0 and boardCoord[2]+board.moveXBoard<=500:
        gameCanvas.move(boardID, board.moveXBoard, 0)

    ballCoord = gameCanvas.coords(ovalID)
    if ballCoord[0]+moveXBall>0 and ballCoord[1]+moveYBall>0 and ballCoord[2]+moveXBall<500 and ballCoord[3]+moveYBall<500:
        gameCanvas.move(ovalID,moveXBall,moveYBall)
        if ballCoord[3] + moveYBall >= 470 and boardCoord[0] + board.moveXBoard <= ballCoord[0] + moveXBall and ballCoord[2] + moveXBall <= boardCoord[2] + board.moveXBoard:
            signX = math.copysign(1, random.random() - 0.5)
            signY = math.copysign(1, random.random() - 0.5)
            moveXBall = (random.random() * 4 + 4) * signX
            moveYBall = (random.random() * 4 + 4) * signY
            realtimeScore += 1
            varLabel.config(text=str(realtimeScore))

    elif ballCoord[0]+moveXBall<=0 or ballCoord[1]+moveYBall>=0 or ballCoord[2]+moveXBall>=500 or ballCoord[3]+moveYBall<=500:
        signX = math.copysign(1, random.random() - 0.5)
        signY = math.copysign(1, random.random() - 0.5)
        moveXBall = (random.random() * 4 + 4)*signX
        moveYBall = (random.random() * 4 + 4)*signY

    if ballCoord[3]+moveYBall >= 480:
        tkinter.messagebox.showinfo(title="🤪",message="Congratulation："+str(realtimeScore)+" !")
        break


    mainWindow.update()
    time.sleep(0.08)

