from mysql.connector import MySQLConnection, Error
import player
import teams
import match
import bowling
import performance
import batting
import sys
sys.path.append("../")
import config

def scrapeAll():
    try:
        conn = MySQLConnection(host = 'localhost', database = config.database, user = config.user, password = config.password)
    except:
        print("MySQL login failed:Update your config.py file")
        exit()
    teams.connect()
    player.connect()
    match.connect()
    batting.connect()
    bowling.connect()
    performance.connect()


if __name__ == "__main__":
    scrapeAll()
