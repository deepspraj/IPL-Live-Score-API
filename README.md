# IPL LIVE SCORE API

[Live](https://ipl-cricket-api.herokuapp.com/) App.


### IPL 2021

API | Description | Auth | HTTPS |
|---|---|---|---|
|[Schedule](https://ipl-cricket-api.herokuapp.com/ipl-2021-schedule) | IPL Schedule | No | Yes |
|[Points Table](https://ipl-cricket-api.herokuapp.com/ipl-2021-points-table) | Points Table | No | Yes |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s1) Server 1 | Live Score | No | Yes |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s2) Server 2 | Live Score | No | Yes |
|[MI Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-mi-squad) | MI Team Members | No | Yes |
|[CSK Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-csk-squad) | CSK Team Members | No | Yes |
|[RR Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-rr-squad) | RR Team Members | No | Yes |
|[RCB Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-rcb-squad) | RCB Team Members | No | Yes |
|[KXIP Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-pl-squad) | KXIP Team Members | No | Yes |
|[DC Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-dc-squad) | DC Team Members | No | Yes |
|[SRH Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-srh-squad) | SRH Team Members | No | Yes |
|[KKR Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-kkr-squad) | KKR Team Members | No | Yes |

<br>

## Sraping Websites 

```
https://www.sportskeeda.com/
https://www.cricket.one/
```

## Sample Response

All response are in JSON (JavaScript Object Notation) Format.

Live Score (server 1)
```
{
  "Match 1": {
    "Team 1": "Chennai Super Kings",
    "1st Innings": "188/7 (20 ov)",
    "Team 2": "Delhi Capitals",
    "2nd Innings": "101/0 (10.1 ov)"
  }
}
```

Live Score (server 2)
```
{
  "Match1": {
    "Team 1": "DC",
    "Score 1": "101/0",
    "Over's 1": "10.1",
    "Team 2": "CSK",
    "Score 2": "188/7",
    "Over's 2": "20.0"
  }
}
```


## Running Locally

Make sure you have [Python](https://www.python.org/) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

```sh

git clone https://github.com/deepspraj/ipl-live-score-api.git # or clone your own fork
cd ipl-live-score-api
pip install -r requirements.txt
python app.py
```

Your app should now be running on [http://localhost:5000](http://localhost:5000/).

<br>

## Deploying to Heroku
```
git add .
git commit -am "realease v1"
git push heroku master
heroku open
```

Alternatively, you can deploy your own copy of the app using this button:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)