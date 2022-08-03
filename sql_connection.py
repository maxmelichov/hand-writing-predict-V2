import mysql.connector
from datetime import datetime
db = mysql.connector.connect(host="localhost",user='root',passwd='1234',database="GameDataBase")
mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE GameDataBase")
# mycursor.execute("DROP TABLE Score")
# mycursor.execute("DROP TABLE Users")
# mycursor.execute("CREATE TABLE Users (Id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(50) NOT NULL)")
# mycursor.execute("CREATE TABLE Scores (userId INT PRIMARY KEY,FOREIGN KEY(userId) REFERENCES Users(Id),Score INT NOT NULL DEFAULT 0)")
# mycursor.execute("INSERT INTO Users (Name) VALUES(%s)",["max"])
mycursor.execute("SELECT * FROM Users")
for x in mycursor:
    print(x)
db.commit()