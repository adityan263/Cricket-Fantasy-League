from mysql.connector import MySQLConnection, Error
import bs4
import requests 
import unicodedata
import sys
sys.path.append("../")
import config

mumurl = ['https://www.iplt20.com/teams/mumbai-indians/squad/91/pradeep-sangwan', 'https://www.iplt20.com/teams/mumbai-indians/squad/1594/mustafizur-rahman', 'http://www.iplt20.com/teams/mumbai-indians/squad/107/Rohit-Sharma/', 'http://www.iplt20.com/teams/mumbai-indians/squad/1124/Jasprit-Bumrah/', 'https://www.iplt20.com/teams/mumbai-indians/squad/3763/rahul-chahar', 'https://www.iplt20.com/teams/mumbai-indians/squad/913/ben-cutting', 'https://www.iplt20.com/teams/mumbai-indians/squad/588/akila-dananjaya', 'https://www.iplt20.com/teams/mumbai-indians/squad/182/jp-duminy', 'https://www.iplt20.com/teams/mumbai-indians/squad/2975/ishan-kishan', 'https://www.iplt20.com/teams/mumbai-indians/squad/872/evin-lewis', 'https://www.iplt20.com/teams/mumbai-indians/squad/4951/mayank-markande', 'https://www.iplt20.com/teams/mumbai-indians/squad/730/mitchell-mcclenaghan', 'https://www.iplt20.com/teams/mumbai-indians/squad/434/adam-milne', 'https://www.iplt20.com/teams/mumbai-indians/squad/2740/hardik-pandya', 'https://www.iplt20.com/teams/mumbai-indians/squad/3183/krunal-pandya', 'https://www.iplt20.com/teams/mumbai-indians/squad/210/kieron-pollard', 'https://www.iplt20.com/teams/mumbai-indians/squad/163/saurabh-tiwary', 'https://www.iplt20.com/teams/mumbai-indians/squad/108/suryakumar-yadav']
cskurl = ['https://www.iplt20.com/teams/chennai-super-kings/squad/297/kedar-jadhav', 'https://www.iplt20.com/teams/chennai-super-kings/squad/2749/mark-wood', 'https://www.iplt20.com/teams/chennai-super-kings/squad/1/ms-dhoni', 'https://www.iplt20.com/teams/chennai-super-kings/squad/898/imran-tahir', 'https://www.iplt20.com/teams/chennai-super-kings/squad/2756/sam-billings', 'https://www.iplt20.com/teams/chennai-super-kings/squad/7/murali-vijay', 'https://www.iplt20.com/teams/chennai-super-kings/squad/9/ravindra-jadeja', 'https://www.iplt20.com/teams/chennai-super-kings/squad/140/deepak-chahar', 'https://www.iplt20.com/teams/chennai-super-kings/squad/14/suresh-raina', 'https://www.iplt20.com/teams/chennai-super-kings/squad/4944/km-asif', 'https://www.iplt20.com/teams/chennai-super-kings/squad/1745/shardul-thakur', 'https://www.iplt20.com/teams/chennai-super-kings/squad/24/faf-du-plessis', 'https://www.iplt20.com/teams/chennai-super-kings/squad/25/dwayne-bravo', 'https://www.iplt20.com/teams/chennai-super-kings/squad/227/shane-watson', 'https://www.iplt20.com/teams/chennai-super-kings/squad/100/ambati-rayudu', 'https://www.iplt20.com/teams/chennai-super-kings/squad/103/harbhajan-singh', 'https://www.iplt20.com/teams/chennai-super-kings/squad/2758/david-willey', 'https://www.iplt20.com/teams/chennai-super-kings/squad/4946/dhruv-shorey', 'https://www.iplt20.com/teams/chennai-super-kings/squad/1118/karn-sharma', 'https://www.iplt20.com/teams/chennai-super-kings/squad/3746/lungi-ngidi']
k11purl = ['https://www.iplt20.com/teams/kings-xi-punjab/squad/3177/akshdeep-nath', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/89/manoj-tiwary', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/2746/barinder-sran', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/158/mayank-agarwal', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/4572/mujeeb-ur-rahman', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/8/ravichandran-ashwin', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/964/marcus-stoinis', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/1125/lokesh-rahul', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/167/aaron-finch', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/1480/andrew-tye', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/236/chris-gayle', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/113/yuvraj-singh', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/1106/ankit-rajpoot', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/1107/mohit-sharma', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/276/karun-nair', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/1113/axar-patel', 'https://www.iplt20.com/teams/kings-xi-punjab/squad/187/david-miller']
kkrurl = ['https://www.iplt20.com/teams/kolkata-knight-riders/squad/102/dinesh-karthik', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/76/piyush-chawla', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/3646/tom-curran', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/213/mitchell-johnson', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/261/kuldeep-yadav', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/179/chris-lynn', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/203/sunil-narine', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/2738/nitish-rana', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/177/andre-russell', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/3779/shivam-mavi', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/3761/shubman-gill', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/127/robin-uthappa', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/4960/javon-searles', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/3779/shivam-mavi', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/166/vinay-kumar', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/5105/prasidh-krishna', 'https://www.iplt20.com/teams/kolkata-knight-riders/squad/3830/rinku-singh']
ddurl = ['https://www.iplt20.com/teams/delhi-daredevils/squad/1563/shreyas-iyer', 'https://www.iplt20.com/teams/delhi-daredevils/squad/836/chris-morris', 'https://www.iplt20.com/teams/delhi-daredevils/squad/773/colin-munro', 'https://www.iplt20.com/teams/delhi-daredevils/squad/969/trent-boult', 'https://www.iplt20.com/teams/delhi-daredevils/squad/84/gautam-gambhir', 'https://www.iplt20.com/teams/delhi-daredevils/squad/1749/rahul-tewatia', 'https://www.iplt20.com/teams/delhi-daredevils/squad/1561/avesh-khan', 'https://www.iplt20.com/teams/delhi-daredevils/squad/282/glenn-maxwell', 'https://www.iplt20.com/teams/delhi-daredevils/squad/2972/rishabh-pant', 'https://www.iplt20.com/teams/delhi-daredevils/squad/30/amit-mishra', 'https://www.iplt20.com/teams/delhi-daredevils/squad/94/mohammed-shami', 'https://www.iplt20.com/teams/delhi-daredevils/squad/1906/jason-roy', 'https://www.iplt20.com/teams/delhi-daredevils/squad/3764/prithvi-shaw', 'https://www.iplt20.com/teams/delhi-daredevils/squad/1083/vijay-shankar', 'https://www.iplt20.com/teams/delhi-daredevils/squad/3013/sandeep-lamichhane', 'https://www.iplt20.com/teams/delhi-daredevils/squad/157/harshal-patel', 'https://www.iplt20.com/teams/delhi-daredevils/squad/3760/abhishek-sharma', 'https://www.iplt20.com/teams/delhi-daredevils/squad/1842/liam-plunkett', 'https://www.iplt20.com/teams/delhi-daredevils/squad/52/naman-ojha', 'https://www.iplt20.com/teams/delhi-daredevils/squad/181/dan-christian', 'https://www.iplt20.com/teams/delhi-daredevils/squad/4277/junior-dala', 'https://www.iplt20.com/teams/delhi-daredevils/squad/57/shahbaz-nadeem']
rrurl = ['https://www.iplt20.com/teams/rajasthan-royals/squad/135/ajinkya-rahane', 'https://www.iplt20.com/teams/rajasthan-royals/squad/509/jos-buttler', 'https://www.iplt20.com/teams/rajasthan-royals/squad/1748/shreyas-gopal', 'https://www.iplt20.com/teams/rajasthan-royals/squad/3834/krishnappa-gowtham', 'https://www.iplt20.com/teams/rajasthan-royals/squad/3869/heinrich-klaasen', 'https://www.iplt20.com/teams/rajasthan-royals/squad/101/dhawal-kulkarni', 'https://www.iplt20.com/teams/rajasthan-royals/squad/921/ben-laughlin', 'https://www.iplt20.com/teams/rajasthan-royals/squad/258/sanju-samson', 'https://www.iplt20.com/teams/rajasthan-royals/squad/3887/d-arcy-short', 'https://www.iplt20.com/teams/rajasthan-royals/squad/1154/ben-stokes', 'https://www.iplt20.com/teams/rajasthan-royals/squad/3838/rahul-tripathi', 'https://www.iplt20.com/teams/rajasthan-royals/squad/86/jaydev-unadkat', 'https://www.iplt20.com/teams/rajasthan-royals/squad/3502/jofra-archer', 'https://www.iplt20.com/teams/rajasthan-royals/squad/148/stuart-binny','https://www.iplt20.com/teams/rajasthan-royals/squad/1304/ish-sodhi','https://www.iplt20.com/teams/rajasthan-royals/squad/3226/prashant-chopra','https://www.iplt20.com/teams/rajasthan-royals/squad/3869/heinrich-klaasen','https://www.iplt20.com/teams/rajasthan-royals/squad/2970/mahipal-lomror']
rcburl =['https://www.iplt20.com/teams/royal-challengers-bangalore/squad/3835/kulwant-khejroliya','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/164/virat-kohli','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/1735/moeen-ali','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/111/yuzvendra-chahal','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/820/colin-de-grandhomme','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/834/quinton-de-kock','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/233/ab-de-villiers','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/1564/sarfaraz-khan','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/202/brendon-mccullum','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/72/mandeep-singh','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/3840/mohammed-siraj','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/44/parthiv-patel','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/307/tim-southee','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/1085/manan-vohra','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/2973/washington-sundar','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/967/chris-woakes','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/59/umesh-yadav','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/3187/murugan-ashwin','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/53/pawan-negi','https://www.iplt20.com/teams/royal-challengers-bangalore/squad/968/corey-anderson']
srhurl = ['https://www.iplt20.com/teams/sunrisers-hyderabad/squad/1521/billy-stanlake', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/440/kane-williamson', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/3825/basil-thampi', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/2722/carlos-brathwaite', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/41/shikhar-dhawan', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/95/shreevats-goswami', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/511/alex-hales', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/1556/deepak-hooda', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/1086/siddarth-kaul', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/116/bhuvneshwar-kumar', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/123/manish-pandey', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/96/yusuf-pathan', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/2885/rashid-khan', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/1112/sandeep-sharma', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/16/wriddhiman-saha', 'https://www.iplt20.com/teams/sunrisers-hyderabad/squad/201/shakib-al-hasan','https://www.iplt20.com/teams/sunrisers-hyderabad/squad/1555/ricky-bhui','https://www.iplt20.com/teams/sunrisers-hyderabad/squad/618/mohammad-nabi']	
urls = [cskurl, ddurl, k11purl, kkrurl, mumurl, rrurl, rcburl, srhurl]

def Player(url):
	sauce = requests.get(url)
	soup = bs4.BeautifulSoup(sauce.text, 'lxml')
	player = []	
	i = 0
	#Player Name

	try :
		name = soup.find('h1', {'class' : 'player-hero__name  player-hero__name--captain'})
		player.append(str(name.text))
	except :
		name = soup.find('h1' , {'class' : 'player-hero__name'})
		player.append(str(name.text))


	#Player Team
	player.append(str(soup.find('div', {'class' : 'team-info'}).find('h1').text))
	
	#Player Batting Style
	try:
		if str(soup.find('table', {'class':'player-details'}).find_all('td', {'class' : 'player-details__value'})[1].text)[:5] == 'Right':
			player.append("RIGHT")
		else:
			player.append("LEFT")
	except : 
		player.append("RIGHT")

	#Player Batting
	table1 = soup.find('table', {'class' : 'table table--scroll-on-phablet player-stats-table'})
	index = [1,3,4,5,7,8,9,10,11]
	row = table1.find('tr', {'class' : 'player-stats-table__highlight'})
	i = 0
	for stat in row.find_all('td'):
		if i in index:
			if '*' in stat.text:
				player.append(str(stat.text[:-1]))
				i += 1
				continue
			if stat.text == '-':
				player.append("0.0")
				i += 1
				continue
			player.append(str(stat.text))
		i += 1
	
	#Player Bowling
	table2 = soup.find_all('table', {'class':'table table--scroll-on-phablet player-stats-table'})[1]
	index = [4, 7, 9, 10]
	row = table2.find('tr', {'class' : 'player-stats-table__highlight'})
	i = 0
	for stat in row.find_all('td'):
		if i in index:
			if stat.text == '-':
				player.append("0.0")
				i += 1
				continue
			player.append(str(stat.text))
		i += 1
	return(player)

def connect() :
	try:
		conn = MySQLConnection(host = 'localhost', database = 'python_mysql', user = 'root', password = 'Frndzz-malife1')
	except:
		conn = MySQLConnection(host = 'localhost', database = config.database, user = config.user, password = config.password)
	team_id = 1
	cursor = conn.cursor()
	for teams in urls:
		for url in teams:
			print(url)
			player = Player(url)
			data = (player[0], team_id, player[2], int(player[3]), int(player[4]), int(player[5]), float(player[6]), float(player[7]), int(player[8]), int(player[9]), int(player[10]), int(player[11]), int(player[12]), float(player[13]), int(player[14]), int(player[15]), 0)
			print(data)
			cursor.execute("INSERT INTO player(name, team_id, batstyle, matches, runs, highest_score, average, strike_rate, hundreds, fifties, fours, sixes, wickets, eco, fourhaul, fivehaul, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
		team_id += 1
	conn.commit()
	cursor.close()
	conn.close()


connect()
