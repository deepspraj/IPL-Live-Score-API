# IPL LIVE SCORE API

[Live](https://ipl-cricket-api.herokuapp.com/) App.


### IPL 2021

API | Description | Auth | HTTPS |
|---|---|---|---|
|[Schedule](https://ipl-cricket-api.herokuapp.com/ipl-2021-schedule) | IPL Schedule | No | Yes |
|[Points Table](https://ipl-cricket-api.herokuapp.com/ipl-2021-points-table) | Points Table | No | Yes |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s1) Server 1 | Live Score | No | Yes |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s2) Server 2 | Live Score | No | Yes |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s3) Server 3 | Live Score | No | Yes |
|[MI Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-mi-squad) | MI Team Members | No | Yes |
|[CSK Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-csk-squad) | CSK Team Members | No | Yes |
|[RR Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-rr-squad) | RR Team Members | No | Yes |
|[RCB Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-rcb-squad) | RCB Team Members | No | Yes |
|[PK Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-pk-squad) | PK Team Members | No | Yes |
|[DC Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-dc-squad) | DC Team Members | No | Yes |
|[SRH Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-srh-squad) | SRH Team Members | No | Yes |
|[KKR Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-kkr-squad) | KKR Team Members | No | Yes |

<br>

## Sraping Websites 

```
https://www.sportskeeda.com
https://www.cricket.one
https://m.cricbuzz.com
```

## Sample Response

All response are in JSON (JavaScript Object Notation) Format.

Match is LIVE

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

Live Score (server 3)
```
{
  "Match 1": {
    "Now": "Rajasthan Royals vs Delhi Capitals",
    "Team 1": "DC",
    "1st innings": "147/8 (20)",
    "Team 2": "RR",
    "2nd innings": "31/3 (7)",
    "CRR": "4.43",
    "RR": "9.00"
  }
}
```
Match END's 

Live Score (server 1)
```
{}
```
Live Score (server 2)
```
{}
```
Live Score (server 3)
```
{}
```

## Latency Status


API | Latency | Requests |
|---|---|---|
|[Schedule](https://ipl-cricket-api.herokuapp.com/ipl-2021-schedule) | <center>611 ms</center> | <center>2</center> |
|[Points Table](https://ipl-cricket-api.herokuapp.com/ipl-2021-points-table) | <center>542 ms</center> | <center>2</center> |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s1) Server 1 | <center>1290 ms</center> | <center>2</center> |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s2) Server 2 | <center>3540 ms</center> | <center>2</center> |
|[Live Score](https://ipl-cricket-api.herokuapp.com/ipl-2021-live-score-s3) Server 3 | <center>491 ms</center> | <center>2</center> |
|[MI Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-mi-squad) | <center>523 ms</center> | <center>2</center> |
|[CSK Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-csk-squad) | <center>514 ms</center> | <center>2</center> |
|[RR Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-rr-squad) | <center>519 ms</center> | <center>2</center> |
|[RCB Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-rcb-squad) | <center>564 ms</center> | <center>2</center> |
|[PK Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-pk-squad) | <center>517 ms</center> | <center>2</center> |
|[DC Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-dc-squad) | <center>544 ms</center> | <center>2</center> |
|[SRH Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-srh-squad) | <center>597 ms</center> | <center>2</center> |
|[KKR Squad](https://ipl-cricket-api.herokuapp.com/ipl-2021-kkr-squad) | <center>773 ms</center> | <center>2</center> |

<br>

All API were pinged from Europe (Germany-Frankfurt) by [SolarWinds Pingdom](https://tools.pingdom.com) dated on 15-04-2021.

Latency status may vary in 10ms to 100ms for every status check.

## Running Locally

Make sure you have [Python](https://www.python.org/) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

```sh

git clone https://github.com/deepspraj/IPL-Live-Score-API.git # or clone your own fork
cd IPL-Live-Score-API
pip install -r requirements.txt
python app.py
```

Your app should now be running on [http://localhost:5000](http://localhost:5000/).

<br>

## Deploying to Heroku
```
git add .
git commit -am "release v1"
git push heroku master
heroku open
```

Alternatively, you can deploy your own copy of the app using this button:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)