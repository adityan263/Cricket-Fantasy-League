DROP TABLE match_team_performance;
DROP TABLE match_player_bat;
DROP TABLE match_player_bowl;
DROP TABLE dismissal;
DROP TABLE player;
DROP TABLE user_group;
DROP TABLE matches;
DROP TABLE groups;
DROP TABLE team;
DROP TABLE users;
DROP TABLE ground;
DROP TABLE userplayer;


CREATE TABLE users(                                                 
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(20) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	email VARCHAR(20) NOT NULL,
	favteam VARCHAR(20) NOT NULL,                          
	username VARCHAR(20) NOT NULL,
	password VARCHAR(20) NOT NULL,
	budget INT NOT NULL,
	points INT NOT NULL
);

CREATE TABLE team(
	team_id INT,
	name VARCHAR(30) NOT NULL,
	win_year VARCHAR(30),
	owner VARCHAR(50),
	coach VARCHAR(30),
	venue VARCHAR(530),
	captain VARCHAR(30),
	PRIMARY KEY(team_id)
);

CREATE TABLE player(
	player_id INT AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	team_id INT NOT NULL,
	batstyle VARCHAR(5) NOT NULL,
	matches INT,
	runs INT,
	highest_score INT,
	average FLOAT,
	strike_rate FLOAT,
	hundreds INT,
	fifties INT,
	fours INT,
	sixes INT,
	wickets INT,
	eco FLOAT,
	fourhaul INT,
	fivehaul INT,
	price INT,
	PRIMARY KEY(player_id),
	FOREIGN KEY (team_id) REFERENCES team(team_id)
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
	dismissal_id INT PRIMARY KEY,
	dismissal_name VARCHAR(10)
);

CREATE TABLE ground(
	ground_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	city VARCHAR(20) NOT NULL,
	country VARCHAR(20) NOT NULL,
	capacity INT
);

CREATE TABLE matches(
	match_id INT PRIMARY KEY AUTO_INCREMENT,
	team1_id INT,
	team2_id INT,
	ground_id INT,
	dates DATE,
	toss INT,
	batfirst INT,
	team_won INT,
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
	ECO FLOAT,
	wides INT,
	noballs INT,
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
	strike_rate FLOAT,	
	dismissal_id INT,
	dismissal_assist INT,
	bowler INT,
	isout INT,
	PRIMARY KEY (player_id, match_id),
	FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
	FOREIGN KEY (player_id) REFERENCES player(player_id),
	FOREIGN KEY (dismissal_id) REFERENCES dismissal (dismissal_id)
);

create table userplayer (user_id INT, player_id INT, primary key (user_id, player_id), foreign key (player_id) references player(player_id) on delete cascade, foreign key (user_id) references users(user_id) on delete cascade);

insert into dismissal values (0, 'Not Out');
insert into dismissal values (1, 'Caught');
insert into dismissal values (2, 'Run Out');
insert into dismissal values (3, 'LBW');
insert into dismissal values (4, 'Bowled');
insert into dismissal values (5, 'Stumped');

insert into ground values (1, 'M. A. Chidambaram Stadium', 'Chennai', 'India', 30000);
insert into ground values (2, 'Feroz Shah Kotla Ground', 'New Delhi', 'India', 31000);
insert into ground values (3, 'IS Bindra Stadium', 'Chandigarh', 'India', 31000);
insert into ground values (4, 'Eden Gardens', 'Kolkata', 'India', 50000);
insert into ground values (5, 'Wankhede Stadium', 'Mumbai', 'India', 30000);
insert into ground values (6, 'Sawai Mansingh Stadium', 'Jaipur', 'India', 22000);
insert into ground values (7, 'M. Chinnaswamy Stadium', 'Bengaluru', 'India', 25000);
insert into ground values (8, 'Rajiv Gandhi International Stadium', 'Hydrabad', 'India', 23000);
insert into ground values (9, 'Sardar Patel Stadium', 'Bengaluru', 'India', 23000);
insert into ground values (10, 'Gahunje Stadium MCA', 'Pune', 'India', 25000);
insert into ground values (11, 'Punjab CA Stadium', 'Bengaluru', 'India', 27000);
insert into ground values (12, 'Vidarbha CA Stadium', 'Nagpur', 'India', 24000);
insert into ground values (13, 'Saurashtra CA', 'Rajkot', 'India', 20000);
insert into ground values (14, 'Melbourne CG', 'Melbourne', 'Australia', 75000);
insert into ground values (15, 'Sydney Cricket', 'Sydney', 'Australia', 60000);
insert into ground values (16, 'WACA Stadium', 'Perth', 'Australia', 40000);
insert into ground values (17, 'Gabba Stadium', 'Brisbane', 'Australia', 50000);
insert into ground values (18, 'Adelaide CG', 'Adelaide', 'Australia', 45000);
insert into ground values (19, 'Blundstone Arena', 'Hobart', 'Australia', 25000);
insert into ground values (20, 'The Oval', 'London', 'England', 45000);
insert into ground values (21, 'Old Trafford', 'Manchester', 'England', 40000);
insert into ground values (22, 'Lords', 'London', 'England', 50000);
insert into ground values (23, 'Trent Bridge', 'Nottingham', 'England', 30000);
insert into ground values (24, 'Headingly', 'Leeds', 'England', 35000);
insert into ground values (25, 'Edgabaston', 'Birmingham', 'England', 42000);
insert into ground values (26, 'Rose Bowl', 'Southamton', 'England', 35000);
insert into ground values (27, 'SuperSport Park', 'Centurion', 'RSA', 15000);
insert into ground values (28, 'Buffalo Park', 'E London', 'RSA', 12000);
insert into ground values (29, 'Newlands', 'Cape Town', 'RSA', 10000);
insert into ground values (30, 'Old Wanderers', 'Johnesburg', 'RSA', 20000);
insert into ground values (31, 'AMI Stadium', 'Christcurch', 'New Zealand', 25000);
insert into ground values (32, 'Basin Reserve', 'Wellington', 'NewZealand', 30000);
insert into ground values (33, 'Craisbrook', 'Dunedin', 'NewZealand', 27000);
insert into ground values (34, 'Kensington Oval', 'Bridgetown', 'WestIndies', 10000);
insert into ground values (35, 'Boruda', 'Guyana', 'WestIndies', 8000);
insert into ground values (36, 'Sabina Park', 'Kingston', 'WestIndies', 13000);
insert into ground values (37, 'Asgiriya Stadium', 'Kandy', 'Sri Lanka', 5000);
insert into ground values (38, 'Colombo Cricket', 'Colombo', 'Sri Lanka', 6000);
insert into ground values (39, 'Dubai International', 'Dubai', 'UAE', 26000);
insert into ground values (40, 'Sharjah Cricket', 'Sharjah', 'UAE', 35000);
