CREATE TABLE users(                                                                                          
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(20) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	favteam VARCHAR(20) NOT NULL,                          
	username VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL 
);

CREATE TABLE team(
	team_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	total_matches INT,
	wins INT,
	points INT
);

CREATE TABLE player(
	player_id INT PRIMARY KEY AUTO_INCREMENT,
	team_id INT NOT NULL,
	debut INT,
	name VARCHAR(30) NOT NULL,
	matches INT,
	batstyle VARCHAR(5) NOT NULL,
	runs INT,
	balls INT,
	highest_score INT,
	fifties INT,
	hundreds INT,
	strike_rate float,
	overs INT,
	wickets INT,
	eco float,
	fivehaul INT,
	tenhaul INT,
	maidens INT,
	price bigINT,
	FOREIGN KEY (team_id) REFERENCES team(team_id),
	FOREIGN KEY (debut) REFERENCES team(team_id)
);

CREATE TABLE groups(
	group_id INT PRIMARY KEY AUTO_INCREMENT,
	groupname VARCHAR(20) NOT NULL
);

CREATE TABLE user_group(
	user_id INT,
	group_id INT,
	FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
	FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE
);

CREATE TABLE dismissal(
	dismissal_id INT PRIMARY KEY AUTO_INCREMENT,
	dismissal_name VARCHAR(10)
);

CREATE TABLE ground(
	ground_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	city VARCHAR(20) NOT NULL,
	country VARCHAR(20) NOT NULL,
	capacity INT
);

CREATE TABLE matches(
	match_id INT PRIMARY KEY AUTO_INCREMENT,
	team1_id INT,
	team2_id INT,
	dates DATE,
	time TIME,
	ground_id INT,
	batfirst INT,
	toss INT,
	MoM INT,
	FOREIGN KEY (team1_id) REFERENCES team(team_id),
	FOREIGN KEY (team2_id) REFERENCES team(team_id),
	FOREIGN KEY (ground_id) REFERENCES ground (ground_id)
);

CREATE TABLE match_team_performance(
	match_id INT,
	team_id INT,
	tot_runs INT,
	tot_wickets INT,
	overs_played INT,
	wides INT,
	noballs INT,
	byes INT,
	legbyes INT,
	PRIMARY KEY (match_id, team_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE match_player_bowl(
	player_id INT,
	match_id INT,
	overs INT,
	maidens INT,
	runs INT,
	wickets INT,
	wides INT,
	noballs INT,
	byes INT,
	legbyes INT,
	PRIMARY KEY (player_id, match_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (player_id) REFERENCES player(player_id)
);

CREATE TABLE match_player_bat(
	player_id INT,
	match_id INT,
	runs INT,
	balls INT,
	fours INT,
	sixes INT,
	dismissal_id INT,
	dismissal_assist INT,
	bowler INT,
	isout INT,
	PRIMARY KEY (player_id, match_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (player_id) REFERENCES player(player_id),
	FOREIGN KEY (dismissal_id) REFERENCES dismissal (dismissal_id)
);
