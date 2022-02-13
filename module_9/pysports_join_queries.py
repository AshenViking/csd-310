#pysports_join_queries
#Carl Young 
#2/13/2022

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
    cursor = db.cursor()

    #display player records
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players=cursor.fetchall()
    print("\n-- DISPLAYING PLAYER RECORDS --")
    for p in players:
        print(" Player ID: {} \n First Name: {} \n Last Name: {} \n Team ID: {} \n".format(p[0], p[1], p[2], p[3]))


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
