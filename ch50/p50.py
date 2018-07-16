import sqlite3
import random
import os


def numerirandom(nn):
    # print (os.getcwd())
    conn = sqlite3.connect('../../git/numeri.db')
    c = conn.cursor()

    # SQL Code
    # Create table
    c.execute("CREATE TABLE if not exists numeri (int numero)")
    #      print ("table numeri created")
    #     i = 1

    # except sqlite3.Error as e:
    #     print ("An error occurred:", e.args[0])
    c.execute("SELECT * from numeri LIMIT  %s;" % nn)
    results = c.fetchall()
    i = len(results)
    listaNum = []
    if nn <= i:
        recin = random.randint(0, i - nn)
    else:
        recin = 0
    reccount = recin + min(nn, i)
    while recin < reccount:
        listaNum.append(results[recin][0])
        recin += 1
    while i < nn:
        recin = random.randint(-1000001, 1000001)
        listaNum.append(recin)
        c.execute("INSERT INTO numeri VALUES (%s)" % recin)  # Insert a row of data
        i += 1
        # Save (commit) the changes
    conn.commit()

    # print(row[0]) # will be a list

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    return listaNum

# print(numerirandom(10))
