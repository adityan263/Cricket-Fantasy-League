import sys

import mysql.connector
conn = mysql.connector.connect(database="cricket", user="root", host="127.0.0.1",
        password="vivbhav97")
cursor = conn.cursor()


team1_name = input("Enter team 1 name")
cursor.execute(("select team_id from team where name = '{}';".format(team1_name)))
team1_id = cursor.fetchone()
print (team1_id)

team2_name = input("Enter team 2 name")
cursor.execute(("select team_id from team where name = '{}';".format(team2_name)))
team2_id = cursor.fetchone()
print (team2_id)

batfirst = input("Enter team 1 or 2 whoever batted first")
if (batfirst == 1):
	batfirst = team1_id
else:
	batfirst = team2_id
print (batfirst)

toss = input("Enter team 1 or 2 whoever won the toss")
if (toss == 1):
	toss = team1_id
else:
	toss = team2_id
print (toss)

won = input("Enter team 1 or 2 whoever won the match")
if (won == 1):
	won = team1_id
else:
	won = team2_id
print (won)

venue_city = input("Enter the name of the city where the match was played")
#venue_id = cursor.execute(("select id from ground where


	cursor.execute(("select password from users where username ='{}';".format(username)))
	a = cursor.fetchone()
	if not a:
        	cursor.execute(("insert into users(username, password,firstname,lastname, email, favteam) values('{}','{}','{}','{}','{}','{}');".format(username, password,firstname,lastname, email, favteam)))
	        cursor.execute(("commit;"))
        	return ("Hello {}, you've successfully registered".format(username))
	else:
        	return ("Username is already taken!")
"""
