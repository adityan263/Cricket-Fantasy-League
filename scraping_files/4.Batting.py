from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata


url0 = ['http://www.espncricinfo.com/series/8048/scorecard/1136561/mumbai-indians-vs-chennai-super-kings-1st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136562/kings-xi-punjab-vs-delhi-daredevils-2nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136563/kolkata-knight-riders-vs-royal-challengers-bangalore-3rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136564/sunrisers-hyderabad-vs-rajasthan-royals-4th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136564/sunrisers-hyderabad-vs-rajasthan-royals-4th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136565/chennai-super-kings-vs-kolkata-knight-riders-5th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136566/rajasthan-royals-vs-delhi-daredevils-6th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136567/sunrisers-hyderabad-vs-mumbai-indians-7th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136568/royal-challengers-bangalore-vs-kings-xi-punjab-8th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136569/mumbai-indians-vs-delhi-daredevils-9th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136572/kings-xi-punjab-vs-chennai-super-kings-12th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136573/kolkata-knight-riders-vs-delhi-daredevils-13th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136575/rajasthan-royals-vs-kolkata-knight-riders-15th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136576/kings-xi-punjab-vs-sunrisers-hyderabad-16th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136578/kolkata-knight-riders-vs-kings-xi-punjab-18th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136579/royal-challengers-bangalore-vs-delhi-daredevils-19th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136582/delhi-daredevils-vs-kings-xi-punjab-22nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136580/sunrisers-hyderabad-vs-chennai-super-kings-20th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136581/rajasthan-royals-vs-mumbai-indians-21st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136583/mumbai-indians-vs-sunrisers-hyderabad-23rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136584/royal-challengers-bangalore-vs-chennai-super-kings-24th-match-indian-premier-league-2018']
url1 = ['http://www.espncricinfo.com/series/8048/scorecard/1136585/sunrisers-hyderabad-vs-kings-xi-punjab-25th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136586/delhi-daredevils-vs-kolkata-knight-riders-26th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136587/chennai-super-kings-vs-mumbai-indians-27th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136588/rajasthan-royals-vs-sunrisers-hyderabad-28th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136589/royal-challengers-bangalore-vs-kolkata-knight-riders-29th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136590/chennai-super-kings-vs-delhi-daredevils-30th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136591/royal-challengers-bangalore-vs-mumbai-indians-31st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136592/delhi-daredevils-vs-rajasthan-royals-32nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136593/kolkata-knight-riders-vs-chennai-super-kings-33rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136594/kings-xi-punjab-vs-mumbai-indians-34th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136595/chennai-super-kings-vs-royal-challengers-bangalore-35th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136596/sunrisers-hyderabad-vs-delhi-daredevils-36th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136597/mumbai-indians-vs-kolkata-knight-riders-37th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136598/kings-xi-punjab-vs-rajasthan-royals-38th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136599/sunrisers-hyderabad-vs-royal-challengers-bangalore-39th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136600/rajasthan-royals-vs-kings-xi-punjab-40th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136601/kolkata-knight-riders-vs-mumbai-indians-41st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136602/delhi-daredevils-vs-sunrisers-hyderabad-42nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136603/rajasthan-royals-vs-chennai-super-kings-43rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136604/kings-xi-punjab-vs-kolkata-knight-riders-44th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136605/delhi-daredevils-vs-royal-challengers-bangalore-45th-match-indian-premier-league-2018']
url2 = ['http://www.espncricinfo.com/series/8048/scorecard/1136606/chennai-super-kings-vs-sunrisers-hyderabad-46th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136607/mumbai-indians-vs-rajasthan-royals-47th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136608/kings-xi-punjab-vs-royal-challengers-bangalore-48th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136609/kolkata-knight-riders-vs-rajasthan-royals-49th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136610/mumbai-indians-vs-kings-xi-punjab-50th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136611/royal-challengers-bangalore-vs-sunrisers-hyderabad-51st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136612/delhi-daredevils-vs-chennai-super-kings-52nd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136613/rajasthan-royals-vs-royal-challengers-bangalore-53rd-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136614/sunrisers-hyderabad-vs-kolkata-knight-riders-54th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136615/delhi-daredevils-vs-mumbai-indians-55th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136616/chennai-super-kings-vs-kings-xi-punjab-56th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136617/sunrisers-hyderabad-vs-chennai-super-kings-qualifier-1-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136618/kolkata-knight-riders-vs-rajasthan-royals-eliminator-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136619/kolkata-knight-riders-vs-sunrisers-hyderabad-qualifier-2-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136620/chennai-super-kings-vs-sunrisers-hyderabad-final-indian-premier-league-2018']
urls = [url0, url1, url2]



def bat(soup) :

	run_list = []
	name_list = []
	out_list = []
	l = []
	#Batsmen Name	
	for link in soup.findAll('div',{'class' : 'cell batsmen'}):
		name_list.append(link.string)

	#Batsmen Runs
	i = 0
	links = soup.find('div', {'class' : 'wrap header'})
	for link in links.find_all('div', {'class' : 'cell runs'}):
		if link.string == 'M':
			break;
		i += 1
	j = 0
	for run in soup.find_all('div', {'class' : 'cell runs'}):
		if j != i:
			runs = run.string
			if runs == '-':
				runs = 0
			run_list.append(runs)
		j += 1
		j %= 5

	#	Not out = 0,  c/b = 1,  Run out = 2,  lbw = 3,  Bowled = 4,  Stumping = 5	
	out = []
	for link in soup.findAll('div', {'class' : "cell commentary"}):
		if link.string:
			out_list.append(link.string)
			continue
		if not link.string :
			out_list.append("a")
			continue
		else :	
			for a in link.find_all('a'):
				out_list.append(a.string)
	for item in out_list:
		items = item.split()
		if 'a' in items:
			out.append('a')
			continue
		if 'not' in items or 'retired' in items:
			out.append([0, 0, 0, 0])
			continue
		isout = 1
		bowler = ''
		dismissal_assist = ''
		if items[0] == 'c':
			dismissal_id = 1
			if items[1] == '&' and items[2] == 'b':
				for i in range(3, len(items)):
					bowler += items[i] + " "
				dismissal_assist = 0 
			else:
				i = 2
				dismissal_assist = items[1]
				while items[i] != 'b':
					dismissal_assist += " " + items[i]
					i += 1
				bowler = items[i + 1]
				for j in range(i + 2, len(items)):
					bowler += " " + items[j]
			out.append([dismissal_id, dismissal_assist, bowler, isout])
			continue
		if items[0] == 'run' and items[1] == 'out':
			dismissal_assist = items[2]
			for i in range(3, len(items)):
				dismissal_assist += " " + items[i]
			dismissal_assist = dismissal_assist[1:-1]
			out.append([2, dismissal_assist, 0, 1])
			continue
		if items[0] == 'lbw' :
			bowler = items[2]
			for i in range(3, len(items)):
				bowler += " " + items[i]
			out.append([3, 0, bowler, 1])
			continue
		if items[0] == 'hit':
			bowler = items[3] + " " + items[4]
			out.append([4, 0, bowler, 1])
		if items[0] == 'b':
			bowler = items[1]
			for i in range(2, len(items)):
				bowler += " " + items[i]
			out.append([4, 0, bowler, 1])
		if items[0] == 'st':
			i = 2
			dismissal_assist = items[1]
			while items[i] != 'b':
				dismissal_assist += " " + items[i]
				i += 1
			bowler = items[i + 1]
			for j in range(i + 2, len(items)):
				bowler += " " + items[j]
			out.append([5, dismissal_assist, bowler, isout])

	for i in range(len(name_list)):
		if name_list[i] == "BATSMEN":
			continue
		player = []
		player.append(name_list[i])
		for j in range(5):
			player.append(run_list[i*5 + j])
		player.extend(out[i])
		l.append(player)
	return l


def find_name(batsman, players, cursor):
	n = batsman.split()
	flag = 0

	if 'Kock' in batsman:
		batsman = 'Quinton de Kock'
	elif 'DJM Short' in batsman or 'Short' in batsman:
		batsman = "D'Arcy Short"
		cursor.execute("select player_id from player where team_id = (select team_id from team where name = 'Rajasthan Royals') and matches = 7;")
		return cursor.fetchone()[0]
	elif 'Williamson' in batsman:
		batsman = 'Kane Williamson'
	elif 'DT Christian' in batsman:
		batsman = 'Dan Christain'
	elif 'Z Khan' in batsman:
		batsman = 'Zaheer Khan'
	elif 'PA Patel' in batsman:
		batsman = 'Parthiv Patel'
	elif 'YK Pathan' in batsman:
		batsman = 'Yusuf Pathan'
	elif 'AR Patel' in batsman:
		batsman = 'Axar Patel'
	elif 'SPD Smith' in batsman:
		batsman = 'Steve Smith'
	elif 'SV Samson' in batsman:
		batsman = 'Sanju Samson'
	elif 'SA Yadav' in batsman:
		batsman = 'Suryakumar Yadav'
	elif 'HH Pandya' in batsman:
		batsman = 'Hardik Pandya'
	elif 'KH Pandya' in batsman:
		batsman = 'Krunal Pandya'
	elif 'Aravind' in batsman:
		batsman = 'Sreenath Arvind'
	elif 'DR Smith' in batsman:
		batsman = 'Dwayne Smith'
	elif 'P Kumar' in batsman:
		batsman = 'Praveen Kumar'
	elif 'B Kumar' in batsman:
		batsman = 'Bhuvneshwar Kumar'
	elif 'I Sharma' in batsman:
		batsman = 'Ishant Sharma'
	elif 'MM Sharma' in batsman:
		batsman = 'Mohit Sharma'
	elif 'KV Sharma' in batsman:
		batsman = 'Karn Sharma'
	elif 'C de Grandhomme' in batsman:
		batsman = 'Colin de Grandhomme'
	elif 'UT Yadav' in batsman:
		batsman = 'Umesh Yadav'
	elif 'CJ Anderson' in batsman:
		batsman = 'Corey Anderson'
	elif 'F du Plessis' in batsman:
		batsman = 'Faf du Plessis'
	elif 'P Negi' in batsman:
		batsman = 'Pavan Negi'
	elif 'M Ashwin' in batsman:
		batsman = 'Murugan Ashwin'
	elif 'IS Sodhi' in batsman:
		batsman = 'Ish Sodhi'
	elif 'P Chopra' in batsman:
		batsman = 'Prashant Chopra'
	elif 'MK Lomror' in batsman:
		batsman = 'Mahipal Lomror'
	name = ''
	for player in players:
		if batsman in player[0]:
			name = player[0]
			flag = 1
			break
	if flag == 0:
		for player in players:
			p = player[0].split()
			if (len(p[1]) > 2 and p[1] in batsman) or (len(p[0]) > 2 and p[0] in batsman):
				name = player[0]
				flag = 1
				break
		if flag == 0:
			print(batsman, 'WTF')
			return 'PAPU'
	cursor.execute("select player_id from player where name = '" + name + "'")
	player_id = cursor.fetchall()[0][0]
	return player_id


def Batting(url, cursor):
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
	team2_id = cursor.fetchone()[0]
		
	#Find all stats
	batsmen = bat(soup)
	cursor.execute("select name from player where team_id = '" + str(team1_id) + "' or team_id = '" + str(team2_id) + "'")
	players = cursor.fetchall()
	for batsman in batsmen :
		player_id = find_name(batsman[0], players, cursor)
		batsman[0] = player_id
		if batsman[0] == 'PAPU':
			continue
		if batsman[8] != 0:
			batsman[8] = find_name(batsman[8], players, cursor)
			if batsman[8] == 'PAPU':
				batsman[8] = 5
		if batsman[7] != 0:
			batsman[7] = find_name(batsman[7], players, cursor)
			if batsman[7] == 'PAPU':
				batsman[7] = 5

	final = []
	for batsman in batsmen:
		if batsman[0] != 'PAPU':
			final.append(batsman)	
	return(final)


def connect() :
	try:
		conn = MySQLConnection(host = 'localhost', database = 'python_mysql', user = 'root', password = 'Frndzz-malife1')
	except:
		conn = MySQLConnection(host = 'localhost', database = 'cricket', user = 'project', password = 'Cricket.1')
	cursor = conn.cursor(buffered = True)
	cursor.execute("select match_id from matches order by match_id limit 1")
	match_id = cursor.fetchone()[0]

	for links in urls:
		for url in links:
			data = []
			print(url)
			items = Batting(url, cursor)
			player_ids = []
			for i in range(len(items)):
				row = (items[i][0], match_id, int(items[i][1]), int(items[i][2]), int(items[i][3]), int(items[i][4]), float(items[i][5]), int(items[i][6]), int(items[i][7]), int(items[i][8]), int(items[i][9]))
				print(row)
				if items[i][0] in player_ids:
					continue
				player_ids.append(items[i][0])
				data.append(row)
			try:
				cursor.executemany("INSERT INTO match_player_bat VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",data)
			except:
				print(data,"foreign key prob")
			match_id += 1
			conn.commit()
	cursor.close()
	conn.close()


connect()



