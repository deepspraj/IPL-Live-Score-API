from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/ipl-2021-schedule')
def ipl_schedule():
    try:
        link = 'https://www.sportskeeda.com/go/ipl/schedule'

        response_sk = requests.get(link)
        all_matches = {}


        if (response_sk.status_code == 200):
                
            sk_html = response_sk.content
            soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')

            dates = []
            time = []
            rival1 = []
            rival2 = []
            location = []

            for date_n_time in soup_sk_obtained.find_all('div', class_='keeda_cricket_event_date'):
                temp = date_n_time.text
                dates.append(temp[1:7])
                time.append(temp[9:17])

            for venue in soup_sk_obtained.find_all('div', class_='keeda_cricket_venue'):
                temp = venue.text
                temp = temp.replace('\n', '')
                location.append(temp[temp.index(',')+2:])

            teams = soup_sk_obtained.find_all('span', class_='keeda_cricket_team_name')
            
            for i in range (len(teams)):
                if  i%2 == 0:
                    temp = teams[i].text
                    rival1.append(temp[1:-1])
                else:
                    temp = teams[i].text
                    rival2.append(temp[1:-1])
            
            

            for i in range (len(rival1)):
                temp1 = rival1[i]
                temp2 = rival2[i]
                all_matches['Match '+ str(i+1)] = { 'Rival' : temp1 + " vs " + temp2, 'Location' : location[i], 'Date' : dates[i], 'Time' : time[i] }


    except:
        
        all_matches = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

    return jsonify(all_matches)


@app.route('/ipl-2021-points-table')
def ipl_points_table():
    try:
        
        link = 'https://www.sportskeeda.com/go/ipl/points-table'

        response_sk = requests.get(link)
        points_table = {}
        teams = []
        played = []
        won = []
        loss = []
        draw = []
        nrr = []
        points = []

        if (response_sk.status_code == 200):
            sk_html = response_sk.content
            soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')
            

            for i in range (1,9):
                team1 = soup_sk_obtained.find_all('tr', id='points_table_' + str(i))


                for date_n_time in team1:            
                    temp = date_n_time.text
                    temp = temp[1:].split('\n')
                    teams.append(temp[4])
                    played.append(temp[7])
                    won.append(temp[8])
                    loss.append(temp[9])
                    draw.append(temp[10])
                    nrr.append(temp[11])
                    points.append(temp[12])


            for i in range (0,8):
                points_table['Team ' + str(i+1)] = { 'Name' : teams[i], 'Played' : int(played[i]), 'Won' : int(won[i]), 'Loss' : int(loss[i]),
                            'Draw' : int(draw[i]), 'Net Run Rate' : float(nrr[i]), 'Points' : float(points[i])}

    except:
        pointsTable = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

    return jsonify(points_table)

@app.route('/ipl-2021-live-score-s1')
def ipl_live_score_s1():

        
    link = 'https://www.sportskeeda.com/go/ipl?ref=carousel'

    response_sk = requests.get(link)
    live_score = {}
    
    if (response_sk.status_code == 200):
        sk_html = response_sk.content
        soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')

        listed_matches = soup_sk_obtained.find_all('div', class_="keeda_cricket_single_match")

        count = 0
        live_match_count = []
        link_all_matches = []
        link_to_scrape = []

        for listed_match in listed_matches:
            if listed_match.find_all('div', class_="live"):
                live_match_count.append(count)

            count += 1



        for live_match in soup_sk_obtained.find_all('a', class_="keeda_cricket_match_link"):
            link_all_matches.append(live_match['href'])


        for i in live_match_count:
            link_to_scrape.append("https://www.sportskeeda.com"+ link_all_matches[i])
        
        
        teams = []
        scores = []
        match = 1

        for link in link_to_scrape:

            response_sk = requests.get(link)
            
            sk_html = response_sk.content
            soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')
            live = soup_sk_obtained.find_all('div', class_="cricket-block score-strip-holder")
            

            for team in live[0].find_all('span', class_="country"):
                temp = team.text
                temp = temp.replace('\n', '')
                teams.append(temp)
            
            for team in live[0].find_all('span', class_="score"):
                temp = team.text
                temp = temp.replace('\n', '')
                scores.append(temp)
            
            if scores[1] == "":
                scores[1] = "N.A"

            
            live_score["Match " + str(match)] = { "Team 1" : teams[0], "1st Innings" : scores[0], "Team 2" : teams[1], "2nd Innings" : scores[1]}  

            teams.clear()
            scores.clear()
            

            match += 1


    return jsonify(live_score)

@app.route('/ipl-2021-live-score-s2')
def ipl_live_score_s2():

    live_score = {}
    
    link = 'https://www.cricket.one/series/804/L3/Indian-Premier-League-2021'

    response_sk = requests.get(link)
    live_score = {}
    
    if (response_sk.status_code == 200):
        sk_html = response_sk.content
        soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')

        listed_matches = soup_sk_obtained.find_all('div', class_="live-matches-schedule")

        match = 1

        for live in listed_matches:

            if live.find_all('div', class_="live-bar"):
                team1 = ''
                team2 = ''
                score1 = 'N.A'
                score2 = 'N.A'
                over1 ='N.A'
                over2 = 'N.A'

                count = 1
                for team in live.find_all('span', class_="team-name"):
                    if count == 1 :
                        team1 = team.text
                    else:
                        team2 = team.text
                    
                    count += 1
                
                count = 1
                for team in live.find_all('span', class_="run-or-out"):
                    if count == 1 :
                        score1 = team.text
                    else:
                        score2 = team.text
                        
                    count += 1
                
                count = 1
                for team in live.find_all('span', class_="over"):
                    if count == 1 :
                        over1 = team.text
                    else:
                        over2 = team.text
                    
                    count += 1

                live_score['Match' + str(match)] = { "Team 1" : team1, "Score 1" : score1, "Over's 1" : over1, "Team 2" : team2, "Score 2" : score2, "Over's 2" : over2 }

    return jsonify(live_score)




@app.route('/ipl-2021-live-score-s3')
def ipl_live_score_s3():
    
    live_score = {}
    
    link = 'https://m.cricbuzz.com/cricket-series/3472/indian-premier-league-2021'

    response_sk = requests.get(link)
    live_score = {}
    
    if (response_sk.status_code == 200):
        sk_html = response_sk.content
        soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')

        listed_matches = soup_sk_obtained.find_all('a', class_="cb-matches-container")

        new_links = []

        for match in listed_matches:

            if match.text[0] == "L":
                new_links.append('https://m.cricbuzz.com' + match['href'])
        
        count = 1

        for link in new_links:
            response_sk = requests.get(link)
            live_score = {}

            comp = ""
            rival1 = ""
            rival2 = ""
            score1 = ""
            score2 = ""
            crr = ""
            rr = ""

            if (response_sk.status_code == 200):
                sk_html = response_sk.content
                soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')

                listed_matches = soup_sk_obtained.find_all('div', class_="col-xs-9 col-lg-9 dis-inline")

                for i in soup_sk_obtained.find_all('h4', class_="cb-list-item ui-header ui-branding-header"):
                    temp = i.text
                    comp, _ = temp.split(',')

                for i in listed_matches[0].find_all('span', class_="teamscores"):
                    temp = i.text
                    rival1, score1 = temp.split('-')
                              
                for i in listed_matches[0].find_all('span', class_="miniscore-teams"):
                    temp = i.text
                    rival2, score2 = temp.split('-')
                
                j = 0
                for i in listed_matches[0].find_all('span', class_="crr"):
                    temp = i.text
                    if j ==0:
                        crr = temp
                        j += 1
                    elif j ==1:
                        rr = temp
                        j += 1
                        
                if rr[2] != ":":
                    live_score['Match ' +str(count)] = { "Now" : comp, "Team 1" : rival1[:-1], "1st innings" : score1[1:], "Team 2" : rival2[:-1], "2nd innings" : score2[1:], crr[:3] : crr[6:], rr[:2] : rr[6:]  }
                else:
                    live_score['Match ' + str(count)] = { "Now" : comp, "Team 1" : rival2[:-1], "Team 1 Score" : score2[1:], crr[:3] : crr[6:]}
                
                count += 1

    return jsonify(live_score)


@app.route("/squad/<string:team_micro>")
def get_squad(team_micro):
    teams = {
        "mi" : "mumbai-indians",
        "rcb" : "royal-challengers-bangalore",
        "csk": "chennai-super-kings",
        "dc" : "delhi-daredevils",
        "pk" : "kings-xi-punjab",
        "kkr" : "kolkata-knight-riders",
        "rr" : "rajasthan-royals",
        "srh" : "sunrisers-hyderabad"
        }


    try:
        team_macro = teams[team_micro.lower()]
        link = 'https://www.sportskeeda.com/team/' + team_macro

        response_sk = requests.get(link)
        squad = {}
            
        if (response_sk.status_code == 200):

            sk_html = response_sk.content
            soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')

            cricket_name = []
            cricketer_role = []
            
            main_section = soup_sk_obtained.find_all('table', class_='stats-table team-table')

            for cricketer in main_section[0].find_all('td', class_='headcol'):
                temp = cricketer.text
                temp = temp.replace('\n', '')
                cricket_name.append(temp)

            for cricketer in main_section[0].find_all('td', class_='secondcol'):
                temp = cricketer.text
                temp = temp.replace('\n', '')
                cricketer_role.append(temp) 
                

            for i in range (len(cricket_name)):
                squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

            squad["status_code"] = 200

    except :
        squad = {
            'status_code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }


    return jsonify(squad)



@app.route('/ipl-winners')
def ipl_winners():

    try:
        link = 'https://www.sportskeeda.com/cricket/ipl-winners-list?ref=carousel'

        response_sk = requests.get(link)
        winners = {}
            
        if (response_sk.status_code == 200):

            sk_html = response_sk.content
            soup_sk_obtained = BeautifulSoup(sk_html,features='html.parser')
            
            main_section = soup_sk_obtained.find_all('tbody')
            winners_list = []
            for section in main_section[0].find_all('td'):
                winners_list.append(section.text)

            for i in range(7,len(winners_list), 7):
                winners['Year ' + str(winners_list[i])] = { 'Winner' : winners_list[i+1], 'Runner UP' : winners_list[i+2], 'Location' : winners_list[i+3]}

    except:
        winners = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }
    return jsonify(winners)




@app.errorhandler(404)
def pageNotFound(e):
    
    error_page = {
            'Status Code' : 404,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, not found url.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

    return jsonify(error_page)

if __name__ == '__main__':
    app.run()
