import mysql.connector
from datetime import datetime
db = mysql.connector.connect(host="localhost",user='root',passwd='1234',database="testdatabase")
mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE testdatabase")
# mycursor.execute("CREATE TABLE Persons (ID INT AUTO_INCREMENT,name VARCHAR(50),age smallint UNSIGNED,PRIMARY KEY (ID))")
# mycursor.execute("INSERT INTO Persons(name,age)VALUES(%s,%s)",("Max",22))
# db.commit()

# mycursor.execute("CREATE TABLE Test (name VARCHAR(50)NOT NULL,created datetime NOT NULL,gender ENUM('M','F')NOT NULL,ID int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Test(name,created,gender) VALUES (%s,%s,%s)",("Joe",datetime.now(),'M'))

# mycursor.execute("SELECT * FROM Persons")
# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY name DESC")
# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL") # add column
# mycursor.execute("ALTER TABLE Test DROP food ") # Drop column
# mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)") # Change the name of the column
# mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(5)") # ERROR because the column is already exits and the size of that CHARVAR is 50!
# mycursor.execute("DESCRIBE Test")



# users=[("Tim","1234"),("Joe","5678"),("Sara","9012")]
# users_scores=[(45,100),(30,200),(46,124)]
# Q1="CREATE TABLE Users(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50),passwd VARCHAR(50))"
# Q2="CREATE TABLE Scores(userId int PRIMARY KEY,FOREIGN KEY(userId) REFERENCES Users(id),game1 int DEFAULT 0,game2 int DEFAULT 0)"
# mycursor.execute(Q1)
# mycursor.execute(Q2)
# mycursor.execute("SHOW TABLES")
# mycursor.executemany("INSERT INTO Users(name,passwd) VALUES (%s,%s)",users)
# for x,user in enumerate(users):
#     mycursor.execute("INSERT INTO Users(name,passwd) VALUES (%s,%s)",user)
#     last_id= mycursor.lastrowid
#     mycursor.execute("INSERT INTO Scores (userID,game1,game2) VALUES (%s,%s,%s)",(last_id,)+users_scores[x])
# db.commit() # SAVE
# mycursor.execute("SELECT * FROM Users")
# for x in mycursor:
#     print(x)

