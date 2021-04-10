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
    try:
        
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

    except:
        live_score = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

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

@app.route('/ipl-2021-mi-squad')
def mumbai_indians_squad():

    try:

        link = 'https://www.sportskeeda.com/team/mumbai-indians'

        response_sk = requests.get(link)
        mi_squad = {}
            
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
                
            temp_dict = {}

            for i in range (len(cricket_name)):
                temp_dict = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

                mi_squad['Player ' + str(i+1)] = temp_dict

    except :
        mi_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }
    return jsonify(mi_squad)


@app.route('/ipl-2021-rcb-squad')
def royal_challengers_bangalore_squad():
    
    try:

        link = 'https://www.sportskeeda.com/team/royal-challengers-bangalore'

        response_sk = requests.get(link)
        rcb_squad = {}
            
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
                rcb_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        rcb_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

    return jsonify(rcb_squad)


@app.route('/ipl-2021-csk-squad')
def chennai_super_kings_squad():
    try:

        link = 'https://www.sportskeeda.com/team/chennai-super-kings'

        response_sk = requests.get(link)
        csk_squad = {}
            
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
                csk_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        csk_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

    return jsonify(csk_squad)



@app.route('/ipl-2021-dc-squad')
def delhi_capitals_squad():
    try:

        link = 'https://www.sportskeeda.com/team/delhi-daredevils'

        response_sk = requests.get(link)
        dc_squad = {}
            
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
                dc_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        dc_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }

    return jsonify(dc_squad)



@app.route('/ipl-2021-pk-squad')
def punjab_kings_squad():
    try:

        link = 'https://www.sportskeeda.com/team/kings-xi-punjab'

        response_sk = requests.get(link)
        pk_squad = {}
            
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
                pk_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        pk_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }


    return jsonify(pk_squad)


@app.route('/ipl-2021-kkr-squad')
def kolkata_knight_riders_squad():
    try:

        link = 'https://www.sportskeeda.com/team/kolkata-knight-riders'

        response_sk = requests.get(link)
        kkr_squad = {}
            
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
                kkr_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        kkr_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }


    return jsonify(kkr_squad)





@app.route('/ipl-2021-rr-squad')
def rajasthan_royals_squad():
    try:

        link = 'https://www.sportskeeda.com/team/rajasthan-royals'

        response_sk = requests.get(link)
        rr_squad = {}
            
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
                rr_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        rr_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }


    return jsonify(rr_squad)




@app.route('/ipl-2021-srh-squad')
def sunrisers_hyderabad_squad():
    try:

        link = 'https://www.sportskeeda.com/team/sunrisers-hyderabad'

        response_sk = requests.get(link)
        srh_squad = {}
            
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
                srh_squad['Player ' + str(i+1)] = { 'Name' : cricket_name[i], 'Role' : cricketer_role[i]}

    except :
        srh_squad = {
            'Status Code' : 500,
            'Title' : 'Something Went Wrong.',
            'Message' : 'Sorry pal, Our servers ran into some problem.',
            'Resolution' : "You can try the search again after few sec or head to the web instead."
            }


    return jsonify(srh_squad)

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