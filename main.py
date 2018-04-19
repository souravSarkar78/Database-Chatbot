import sqlite3

mydb = sqlite3.connect('data.db')
c = mydb.cursor()

c.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER, key TEXT, reply TEXT, PRIMARY KEY(id))")
#c.execute("INSERT INTO data(id, key, reply) VALUES(0, 0, 0)")   #Comment this line after creating the database for the first time
c.execute('SELECT MAX(id) AS MAX FROM data')
for r in c.fetchall():
    ID = r[0]

while True:

    def inputs(id, key, reply):
        cmd = "INSERT INTO data(id, key, reply) VALUES("+str(id)+','+str(key)+','+str(reply)+')'
        print(cmd)
        c.execute(cmd)

    ID +=1
    KEY = input("Enter key: ")
    REPLY = input("Enter reply: ")
    inputs(ID, KEY, REPLY)
    mydb.commit()
