import sqlite3
mydb = sqlite3.connect('data.db')
c = mydb.cursor()

c.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER, key TEXT, reply TEXT, PRIMARY KEY(id))")

print("Welcome Sourav!!!!")
def search(ID):
    cmd = "SELECT * FROM data where id =" + str(ID)
    profile = None
    cursor = c.execute(cmd)
    for row in cursor:
        profile = row
    return profile

c.execute('SELECT MAX(id) AS MAX FROM data')
for r in c.fetchall():
    ID = r[0]

#print(ID)
while True:
    your_input = input("You:  ")

    while True:

        profile = search(ID)
        key = str(profile[1])
        reply = str(profile[2])
        #print (ID)
        ID-=1

        if key in your_input:
            print ("Bot:  ",reply)
        '''if key not in g:
            print("Sorry i didn't understand!")
            ID = 0'''

        if ID==0:
            c.execute('SELECT MAX(id) AS MAX FROM data')
            for r in c.fetchall():
                ID = r[0]
            your_input = input("You:  ")
    #print(key, reply)


mydb.commit()
