
import sqlite3

#conn is variable that holds the connection to the database
#call the class then connect to the database
#creates the database as well
conn = sqlite3.connect('assignment1.db')

#opens the connection
with conn:
    #cursor operates the database when commands are given
    #cur = shortened way to call conn.cursor without typing it out everytime
    cur = conn.cursor() 
    #the sql statement that we will be passing into the execute function
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT, \
        col_ext TEXT \
        )")
    conn.commit()

conn = sqlite3.connect('assignment1.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#sends and execute SQL command to query our database to return specific information to return back to us
for x in fileList:
    if x.endswith('.txt'): 
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_ext) VALUES (?)", (x,))
            print(x)
conn.close()
    
    
    
    
    
 
    
