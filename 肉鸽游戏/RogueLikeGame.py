import tkinter
from PIL import Image, ImageTk
import matplotlib.pyplot

mainWindow = tkinter.Tk()
mainWindow.title("小仙鹤的肉鸽游戏")

mainWindow.state("zoomed")   #窗口全屏显示

windowWidth, windowHeight = mainWindow.maxsize()   #全屏大小
gameCanvas = tkinter.Canvas(mainWindow, width=windowWidth, height=windowHeight)
gameCanvas.pack()

image1 = Image.open("./bjt1.gif")
image1 = image1.resize((400, 400))
image1 = ImageTk.PhotoImage(image1)
image1_1 = gameCanvas.create_image(-100,-100,anchor='nw',image=image1)

image2 = Image.open("./bjt1.gif")
image2 = image2.resize((400, 400))
image2= image2.transpose(Image.FLIP_LEFT_RIGHT)
image2 = ImageTk.PhotoImage(image2)
image2_2 = gameCanvas.create_image(300,-100,anchor='nw',image=image2)

image3 = Image.open("./bjt1.gif")
image3 = image3.resize((400, 400))
image3 = ImageTk.PhotoImage(image3)
image3_3 = gameCanvas.create_image(700,-100,anchor='nw',image=image3)

image4 = Image.open("./bjt1.gif")
image4 = image4.resize((400, 400))
image4 = ImageTk.PhotoImage(image4)
image4_4 = gameCanvas.create_image(1100,-100,anchor='nw',image=image4)

image5 = Image.open("./bjt1.gif")
image5 = image5.resize((400, 400))
image5 = image5.transpose(Image.FLIP_LEFT_RIGHT)
image5 = ImageTk.PhotoImage(image5)
image5_5 = gameCanvas.create_image(-100,300,anchor='nw',image=image5)

image6 = Image.open("./bjt1.gif")
image6 = image6.resize((400, 400))
image6 = ImageTk.PhotoImage(image6)
image6_6 = gameCanvas.create_image(300,300,anchor='nw',image=image6)

image7 = Image.open("./bjt1.gif")
image7 = image7.resize((400, 400))
image7 = ImageTk.PhotoImage(image7)
image7_7 = gameCanvas.create_image(700,300,anchor='nw',image=image7)

image8 = Image.open("./bjt1.gif")
image8 = image8.resize((400, 400))
image8= image8.transpose(Image.FLIP_LEFT_RIGHT)
image8 = ImageTk.PhotoImage(image8)
image8_8 = gameCanvas.create_image(1100,300,anchor='nw',image=image8)

mainWindow.mainloop()
