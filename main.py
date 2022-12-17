import requests
from bs4 import BeautifulSoup as bss4
from csv import writer

url = requests.get("https://www.yallakora.com/world-cup/2767/Scorers/%D9%83%D8%A3%D8%B3-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85#HPStatsClipScorers")

soup = bss4(url.content, 'html.parser')

players= soup.findAll('div' , {'class' : 'wRow item page-1'})
with open('plaing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['name', 'nationality', 'goal']

    thewriter.writerow(header)

for player in players:
    player_name = player.find('p').text
    player_nationality = player.find('div','item team').text.replace('\n', '')
    the_num_of_goal = player.find('div', 'item dtls').text.replace('\n', '')
    info = [player_name] , [player_nationality] , [the_num_of_goal]
    print(info)
