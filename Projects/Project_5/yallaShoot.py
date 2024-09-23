from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://shootz.yalla-shoot-tv.live/home18/').text
soup = BeautifulSoup(page, 'lxml')

matches = soup.find_all('div', class_ = 'match-container')

matches_details = []

for match in matches :
    team1 = match.find('div', class_= 'left-team').text.strip()
    team2 = match.find('div', class_= 'right-team').text.strip()
    
    match_time = match.find('div', class_ = 'match-timing').text.strip()
    
    matches_details.append([team1, team2, match_time])
    
with open('yalla_shoot_matches.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Team 1', 'Team 2', 'Match Time'])
    writer.writerows(matches_details)
    
print("Data scraped and saved to matches.csv")

    
