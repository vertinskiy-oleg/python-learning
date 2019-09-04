import sqlite3
#Create connection to a db or create a new db
conn = sqlite3.connect('users.db')

#Create cursor object
c = conn.cursor()

#Execute SQL queries

#Create Table
# c.execute('''CREATE TABLE users 
#               (id INTEGER, name TEXT, age INTEGER);''')

#Insert 1 value with ? variables
# user = (1, 'John', 30)
# query = '''INSERT INTO users 
#             VALUES (?, ?, ?)'''
#c.execute(query, user) # values will be inserted instead of ? in query from user tuple


users = [(2, 'Bob', 45),
        (3, 'Mary', 25),
        (4, 'Jane', 40),
        (5, 'Lizy', 5)]

query = '''INSERT INTO users 
            VALUES (?, ?, ?)'''

#Bulk insert using executemany() method
#c.executemany(query, users) # values will be inserted instead of ? from all tuples in users list

#Bulk insert using for loop
# for user in users:
#     c.execute(query, user)

#Selecting from tables
name = ('John',) #variables for SQL queries must be in a tuple
# result = c.execute("SELECT * FROM users;")
result = c.execute("SELECT * FROM users WHERE name =?;", name) #selecting with variable
print(result.fetchone()) # return the first result as a tuple
print(result.fetchall()) # return all results as tuples in a list

#Commit changes and close db
conn.commit()
conn.close()