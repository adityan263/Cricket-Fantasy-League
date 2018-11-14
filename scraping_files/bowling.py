from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
#import python_mysql_dbconfig 


url0 = ['http://www.espncricinfo.com/series/8048/scorecard/1136561/mumbai-indians-vs-chennai-super-kings-1st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136562/kings-xi-punjab-vs-delhi-daredevils-2nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136563/kolkata-knight-riders-vs-royal-challengers-bangalore-3rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136564/sunrisers-hyderabad-vs-rajasthan-royals-4th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136565/chennai-super-kings-vs-kolkata-knight-riders-5th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136566/rajasthan-royals-vs-delhi-daredevils-6th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136567/sunrisers-hyderabad-vs-mumbai-indians-7th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136568/royal-challengers-bangalore-vs-kings-xi-punjab-8th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136569/mumbai-indians-vs-delhi-daredevils-9th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136572/kings-xi-punjab-vs-chennai-super-kings-12th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136573/kolkata-knight-riders-vs-delhi-daredevils-13th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136575/rajasthan-royals-vs-kolkata-knight-riders-15th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136576/kings-xi-punjab-vs-sunrisers-hyderabad-16th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136578/kolkata-knight-riders-vs-kings-xi-punjab-18th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136579/royal-challengers-bangalore-vs-delhi-daredevils-19th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136582/delhi-daredevils-vs-kings-xi-punjab-22nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136580/sunrisers-hyderabad-vs-chennai-super-kings-20th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136581/rajasthan-royals-vs-mumbai-indians-21st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136583/mumbai-indians-vs-sunrisers-hyderabad-23rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136584/royal-challengers-bangalore-vs-chennai-super-kings-24th-match-indian-premier-league-2018']
url1 = ['http://www.espncricinfo.com/series/8048/scorecard/1136585/sunrisers-hyderabad-vs-kings-xi-punjab-25th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136586/delhi-daredevils-vs-kolkata-knight-riders-26th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136587/chennai-super-kings-vs-mumbai-indians-27th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136588/rajasthan-royals-vs-sunrisers-hyderabad-28th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136589/royal-challengers-bangalore-vs-kolkata-knight-riders-29th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136590/chennai-super-kings-vs-delhi-daredevils-30th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136591/royal-challengers-bangalore-vs-mumbai-indians-31st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136592/delhi-daredevils-vs-rajasthan-royals-32nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136593/kolkata-knight-riders-vs-chennai-super-kings-33rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136594/kings-xi-punjab-vs-mumbai-indians-34th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136595/chennai-super-kings-vs-royal-challengers-bangalore-35th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136596/sunrisers-hyderabad-vs-delhi-daredevils-36th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136597/mumbai-indians-vs-kolkata-knight-riders-37th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136598/kings-xi-punjab-vs-rajasthan-royals-38th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136599/sunrisers-hyderabad-vs-royal-challengers-bangalore-39th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136600/rajasthan-royals-vs-kings-xi-punjab-40th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136601/kolkata-knight-riders-vs-mumbai-indians-41st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136602/delhi-daredevils-vs-sunrisers-hyderabad-42nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136603/rajasthan-royals-vs-chennai-super-kings-43rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136604/kings-xi-punjab-vs-kolkata-knight-riders-44th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136605/delhi-daredevils-vs-royal-challengers-bangalore-45th-match-indian-premier-league-2018']
url2 = ['http://www.espncricinfo.com/series/8048/scorecard/1136606/chennai-super-kings-vs-sunrisers-hyderabad-46th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136607/mumbai-indians-vs-rajasthan-royals-47th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136608/kings-xi-punjab-vs-royal-challengers-bangalore-48th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136609/kolkata-knight-riders-vs-rajasthan-royals-49th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136610/mumbai-indians-vs-kings-xi-punjab-50th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136611/royal-challengers-bangalore-vs-sunrisers-hyderabad-51st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136612/delhi-daredevils-vs-chennai-super-kings-52nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136613/rajasthan-royals-vs-royal-challengers-bangalore-53rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136614/sunrisers-hyderabad-vs-kolkata-knight-riders-54th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136615/delhi-daredevils-vs-mumbai-indians-55th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136616/chennai-super-kings-vs-kings-xi-punjab-56th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136617/sunrisers-hyderabad-vs-chennai-super-kings-qualifier-1-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136618/kolkata-knight-riders-vs-rajasthan-royals-eliminator-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136619/kolkata-knight-riders-vs-sunrisers-hyderabad-qualifier-2-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136620/chennai-super-kings-vs-sunrisers-hyderabad-final-indian-premier-league-2018']
urls = [url0, url1, url2]

def find_bowlers(soup) :
	ball_list = []
	ball = []
	j = 0
	for table in soup.find_all('table'):
		if j == 2:
			break
		j += 1
		table_rows = table.find_all('tr')
		for tr in table_rows:
			td = tr.find_all('td')
			row = [i.text for i in td]
			ball_list.append(row)
	for i in range(len(ball_list)):
		player = []
		if ball_list[i] == []:
			continue
		if len(ball_list[i]) == 10:
			for j in range(len(ball_list[i])-1):
				if (j != 1):
					player.append(str(ball_list[i][j]))
		else :
			for j in range(len(ball_list[i])-1):
				if (j != 1 and j != 7 and j != 8 and j != 9):
					player.append(str(ball_list[i][j]))
			
		ball.append(player)
	return ball

def Bowler(url, cursor):
	team_list = []
	
	#Soup Object
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')

	#FIND NAMES OF TEAMS
	team_list = []
	count = 0
	for name in soup.find_all('a', {'class' : 'app_partial'}):
                for teams in name.find_all('span', {'class' : 'cscore_name cscore_name--long'}):
			count += 1
			if count > 2:
				break
			for team in teams:
				team_list.append(str(team.string))

	#FIND ID OF TEAM
	cursor.execute("select team_id from team where name = '" + team_list[0] + "'")
	team1_id = cursor.fetchone()[0]
	cursor.execute("select team_id from team where name = '" + team_list[1] + "'")
	team2_id = cursor.fetchall()[0][0]
		

	#Find all stats
	bowlers = find_bowlers(soup)
	cursor.execute("select name from player where team_id = '" + str(team1_id) + "' or team_id = '" + str(team2_id) + "'")
	players = cursor.fetchall()


	for bowler in bowlers :
		n = bowler[0].split()
		flag = 0
		if 'Kock' in bowler[0]:
			bowler[0] = 'Quinton de Kock'
		elif 'DJM Short' in bowler[0] or 'Short' in bowler[0]:
			bowler[0] = "D'Arcy Short"
			cursor.execute("select player_id from player where team_id = (select team_id from team where name = 'Rajasthan Royals') and matches = 7;")
			return cursor.fetchone()[0]
		elif 'Williamson' in bowler[0]:
			bowler[0] = 'Kane Williamson'
		elif 'DT Christian' in bowler[0]:
			bowler[0] = 'Dan Christain'
		elif 'Z Khan' in bowler[0]:
			bowler[0] = 'Zaheer Khan'
		elif 'PA Patel' in bowler[0]:
			bowler[0] = 'Parthiv Patel'
		elif 'YK Pathan' in bowler[0]:
			bowler[0] = 'Yusuf Pathan'
		elif 'AR Patel' in bowler[0]:
			bowler[0] = 'Axar Patel'
		elif 'SPD Smith' in bowler[0]:
			bowler[0] = 'Steve Smith'
		elif 'SV Samson' in bowler[0]:
			bowler[0] = 'Sanju Samson'
		elif 'SA Yadav' in bowler[0]:
			bowler[0] = 'Suryakumar Yadav'
		elif 'HH Pandya' in bowler[0]:
			bowler[0] = 'Hardik Pandya'
		elif 'KH Pandya' in bowler[0]:
			bowler[0] = 'Krunal Pandya'
		elif 'Aravind' in bowler[0]:
			bowler[0] = 'Sreenath Arvind'
		elif 'DR Smith' in bowler[0]:
			bowler[0] = 'Dwayne Smith'
		elif 'P Kumar' in bowler[0]:
			bowler[0] = 'Praveen Kumar'
		elif 'B Kumar' in bowler[0]:
			bowler[0] = 'Bhuvneshwar Kumar'
		elif 'I Sharma' in bowler[0]:
			bowler[0] = 'Ishant Sharma'
		elif 'MM Sharma' in bowler[0]:
			bowler[0] = 'Mohit Sharma'
		elif 'KV Sharma' in bowler[0]:
			bowler[0] = 'Karn Sharma'
		elif 'C de Grandhomme' in bowler[0]:
			bowler[0] = 'Colin de Grandhomme'
		elif 'UT Yadav' in bowler[0]:
			bowler[0] = 'Umesh Yadav'
		for player in players:
			if bowler[0] in player[0]:
				name = player[0]
				flag = 1
				break
		if flag == 0:
			for player in players:
				if n[1] in player[0]:
					name = player[0]
					flag = 1
					break
			if flag == 0:
				bowler[0] = 'PAPU'
				continue
		cursor.execute("select player_id from player where name = '" + name + "'")
		player_id = cursor.fetchall()[0][0]
		bowler[0] = player_id

	final = []
	for bowler in bowlers:
		if not bowler[0] == 'PAPU':
			final.append(bowler)	
	return(final)


def connect() :	
	#Connect to Database
	conn = MySQLConnection(host = 'localhost', database = 'python_mysql', user = 'root', password = 'Frndzz-malife1')
	cursor = conn.cursor()
	cursor.execute("select match_id from matches order by match_id limit 1")
	match_id = cursor.fetchone()[0]

	for links in urls:
		for url in links:
			data = []
			print(url)
			items = Bowler(url, cursor)
			print(items)
			try:
				for i in range(len(items)):
					row = (items[i][0], match_id, int(float(items[i][1])), int(items[i][2]), int(items[i][3]), int(items[i][4]), float(items[i][5]), int(items[i][6]), int(items[i][7]))
					data.append(row)
				cursor.executemany("INSERT INTO match_player_bowl VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",data)
				conn.commit()
			except:
				print("nai")
			match_id += 1
	cursor.close()
	conn.close()

connect()



