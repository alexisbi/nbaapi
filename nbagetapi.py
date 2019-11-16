import requests

response = requests.get("http://data.nba.net/prod/v1/11152019/0021900173_boxscore.json")
print(response)