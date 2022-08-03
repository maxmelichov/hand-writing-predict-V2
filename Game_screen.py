from tkinter import *
import win32gui
from PIL import ImageGrab
import predictCNN,login_screen,sql_connection,user
import random
class Game(login_screen.App,object):
    def __init__(self, root,player):
        self.player= player
        self.x = self.y = 0
        self.root= root
        self.canvas = Canvas(root, height=200, width=200, bg="white", cursor="cross")
        self.canvas.bind('<B1-Motion>',self.addLine)
        self.canvas.place(x=0,y=0)
        self.canvas.grid(row=0, column=0, pady=2, sticky=W )
        self.showName()
        self.showScore()
        self.button2= Button(root, text="Clear", font=('Helvetica bold', 10), command = self.reset,background= 'green')
        self.button3= Button(root, text="Quit", font=('Helvetica bold', 10), command = self.quit,background='red')
        
        self.button2.place(x=100,y=220)
        self.button3.place(x=10,y=220)
        self.count =0 
        self.challenge= Button(root, text="Challenge", font=('Helvetica bold', 10), command = self.randomfunc,background="lightblue")
        self.challenge.place(x=250,y=100)
    # def locate_xy(self,event):
    #     global current_x,current_y
    #     current_x,current_y=event.x,event.y

    
    #  draw func
    def addLine(self,event):
        self.x = event.x
        self.y = event.y
        r=7 # width of the line
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
    # label for the challenge 
    def randomfunc(self):
        self.button1= Button(self.root, text="Predict", command=self.predictCNN)
        self.button1.place(x=260,y=30)
        self.num = random.randint(0,9)

        self.rand = Label(self.root,text="Please Draw The Number: "+ str(self.num),font=("Helvetica", 10))
        self.rand.place(x=210,y=130)    
        
    # pred func
    def predictCNN(self):
        HWND = self.canvas.winfo_id() 
        rect = win32gui.GetWindowRect(HWND) 
        img = ImageGrab.grab(rect)
        dig,acc = predictCNN.loadimg(img)
        self.count+=1
        self.label =Label(self.root,text= str(dig)+', '+ str(int(acc*100))+'%'+',attempts:'+str(self.count),font=("Helvetica", 12))
        self.label.place(x=250,y=60)
        self.check(dig)

    def showScore(self):
        self.scoreL= Label(self.root,text="Your score is: " + str(self.player.get_score()) ,font=("Helvetica", 10))
        self.scoreL.place(x=240,y=180)

    def showName(self):
        self.nameLabel= Label(self.root,text="Welcome Back " + str.upper(self.player.get_name()) ,font=("Helvetica", 10))
        self.nameLabel.place(x=230,y=10)

    def score(self):
        self.player.set_score(self.player.get_score()+100)
        sql_connection.mycursor.execute(f"UPDATE Scores SET Score = '{self.player.get_score()}' WHERE userId = '{self.player.get_id()}' ") 
        sql_connection.mycursor.fetchall()
        sql_connection.db.commit()
        self.scoreL.destroy()
        self.showScore()

    def check(self,dig):
        if self.num == dig:
            self.checkl = Label(self.root,text="Good job!!!",font=("Helvetica", 10))
            self.checkl.config(bg="green")
            self.checkl.place(x=250,y=160)   
            self.score()
        else:
            self.checkl = Label(self.root,text="Try Again :(",font=("Helvetica", 10))
            self.checkl.config(bg="red")
            self.checkl.place(x=250,y=160)  
            
    # reset GUI
    def reset(self):
        self.canvas.delete('all')
        self.label.destroy()
        self.rand.destroy()
        self.checkl.destroy()
    # quit GUI
    def quit(self):
        self.root.destroy() 

