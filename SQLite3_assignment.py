import sqlite3
connection = sqlite3.connect("C:\Users\jalen\Documents\GitHub\Python-Projects/test.db")

# This line instantiates a Cursor object. A cursor is a control structure that enables operations on a database. 
# Our Cursor object 'c' will let us execute commands on our SQL database 'test_database' and return the results.
# Now we can easily execute regular SQL statements on the database through the cursor. 
c = connection.cursor()


# This line creates a new table named People and inserts three new columns into the table: 
# text for storing each person’s FirstName, another text field to store the LastName, and an integer to store Age
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

# Here we’ve inserted a new row, with a FirstName of Ron, a LastName of Obvious, and an Age equal to 42.
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit
connection.close()

#perform any SQL operation using connection here
with sqlite3.connect("test_database.db") as connection: