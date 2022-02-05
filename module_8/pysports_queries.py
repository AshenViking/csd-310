#pysports_queries
#Carl Young 
#2/4/2022

import mysql.connector
from mysql.connector import errorcode

config={
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    #print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
   
    #display team records
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams=cursor.fetchall() 
    print("\n -- DISPLAYING TEAM RECORDS --")
    for t in teams:
        print("  Team ID: {} \n Team Name:{} \n Mascot: {} \n".format(t[0], t[1], t[2]))
    
    #display player records
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players=cursor.fetchall()
    print("\n-- DISPLAYING PLAYER RECORDS --")
    for p in players:
        print("  Player ID: {} \n First Name: {} \n Last Name: {} \n Team ID: {} \n".format(p[0], p[1], p[2], p[3]))


    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("     The supplied username or pasword are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("     The specified database does ot exits")
    else:
        print(err)

finally:
    db.close()


