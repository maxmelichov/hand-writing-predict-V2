from tkinter import *
import user,Game_screen,sql_connection
import numpy as np
class App(object):
    def __init__(self, root):
        self.HelloL= Label(root,text="Are you ready to play?",font=("Helvetica", 20))
        self.NameL= Label(root,text="Enter your name",font=("Helvetica", 10))
        self.NameT = Text (root,height=2,width=40,font=("Helvetica", 10))
        self.EnterB= Button(root, text = "Next",command =self.play,font=("Helvetica", 10))
        self.quitB = Button(root, text = "Quit",command =self.quit,font=("Helvetica", 10),background='red')
        self.HelloL.pack()
        self.NameL.pack()
        self.NameT.pack()
        self.EnterB.pack()
        self.quitB.pack()
        self.quitB.place(x=10,y=215)
        self.root= root

    def play(self):
        name=self.NameT.get("1.0", "end-1c")
        sql_connection.mycursor.execute(f"SELECT Name FROM Users WHERE '{name}'= Name")
        myresult=sql_connection.mycursor.fetchall()
        if len(myresult)==0:
            sql_connection.mycursor.execute("INSERT INTO Users (Name) VALUES(%s)",[name])
            self.getId(name)
            sql_connection.mycursor.execute("INSERT INTO Scores (userId,Score) VALUES(%s,%s)",[self.id,0])
            self.connectSQL(name)
        else: 
            self.getId(name)
            self.connectSQL(name)

        self.NewWin()

    def getId(self,name):
        sql_connection.mycursor.execute(f"SELECT Id FROM Users WHERE '{name}'= Name")
        self.id = sql_connection.mycursor.fetchall()
        self.id = [j for i in  self.id for j in i]
        self.id = self.id[0]
       
        
    def connectSQL(self,name):
        self.player= user.User(name,self.id)
        sql_connection.mycursor.execute(f"SELECT Score FROM Scores WHERE '{self.id}' = userId")
        score =sql_connection.mycursor.fetchall()
        score = [j for i in score for j in i]
        score = score[0]
        self.player.set_score(score)
        sql_connection.db.commit()
        return self.player

    def quit(self):
        self.root.destroy() 

    def NewWin(self):
        newWindow = Toplevel(root)
        Geometry(newWindow)
        newWindow.title("Hand-Write Predict")
        game =Game_screen.Game(newWindow,self.player)

def Geometry(master):
    w = 400 # width for the Tk root
    h = 250 # height for the Tk root
    ws = master.winfo_screenwidth() 
    hs = master.winfo_screenheight() 
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    

if __name__ == '__main__':
    root = Tk()
    Geometry(root)
    root.title("Hello Screen")
    app = App(root)
    root.mainloop()