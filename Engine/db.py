import csv
import sqlite3

conn = sqlite3.connect("fido.db")

cusrsor = conn.cursor()

#query ="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), path VARCHAR(1000))"
#cusrsor.execute(query)

#query = "INSERT INTO users VALUES(null,'Brave','//Applications//Brave Browser.app')"
#cusrsor.execute(query)
#conn.commit()

#query = "CREATE TABLE IF NOT EXISTS web_commands (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), path VARCHAR(1000))"
#cusrsor.execute(query)

#query = "INSERT INTO web_commands VALUES(null,'Youtube','https://www.youtube.com/')"
#cusrsor.execute(query)
#conn.commit()

#create  a table with desired columns
#cusrsor.execute("CREATE TABLE IF NOT EXISTS Contact (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)")
#desired_columns_indices = [0 , 18]  # Indices of the columns you want to select (0-based index)
#Read data form the csv file 
#with open('contacts.csv', 'r' , encoding='utf-8') as csvfile:
   # csvreader= csv.reader(csvfile)
    #for row in csvreader:
     #   selected_data = [row[i] for i in desired_columns_indices]
      #  cusrsor.execute("INSERT INTO Contact ('id' , 'name', 'mobile_no') VALUES (NULL,?, ?);", tuple(selected_data))

#commit changes and close the connection
#conn.commit()
#conn.close()


#if you want single single contact to be added
#qurey = "INSERT INTO Contact VALUES(null,'John Doe','1234567890')"
#cusrsor.execute(qurey)
#conn.commit()
#conn.close()
# 
#    