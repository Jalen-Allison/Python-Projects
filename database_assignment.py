
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
conn.close()

conn = sqlite3.connect('assignment1.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('information', 'docx'))
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('Hello', 'txt'))
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('myImage', 'png'))
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('myMovie', 'mpg'))
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('World', 'txt'))
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('data', 'pdf'))
    cur.execute("INSERT INTO tbl_files(col_name, col_ext) VALUES (?,?)" , \
                ('myPhoto', 'jpg'))
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment1.db')

#sends and execute SQL command to query our database to return specific information to return back to us
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_name,col_ext FROM tbl_files WHERE col_ext = 'txt'")
    #store in a variable so it is no longer volatile
    #so when we catch the information it stays and the information wont be lost 
    varFile = cur.fetchmany(2)      
    for item in varFile:
        msg = "File Name: {}\nFile Ext: {}".format(item[0],item[1])
        print(msg)
    
