from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.yallakora.com/Match-Center/?date=18/21/2023'

website = requests.get(url)

soup = BeautifulSoup(website.content, 'html.parser')

championships = soup.find_all('div', class_ = 'matchCard')

with open('matches.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Championship', 'Team A', 'Score', 'Team B', 'Time'])

    for i in range(len(championships)):
        championship_name = championships[i].contents[1].find('h2').text.strip()
        
        matches = championships[i].contents[3].find_all('div', class_='teamCntnr')
        for j in range(len(matches)):
            teamA = matches[j].find('div', {'class':'teamA'}).text.strip()
            teamB = matches[j].find('div', {'class':'teamB'}).text.strip()

            results = matches[j].find('div', {'class':'MResult'}).find_all('span', {'class':'score'})
            score = f'{results[0].text.strip()} - {results[1].text.strip()}'

            time = matches[j].find('div', {'class':'MResult'}).find('span', {'class':'time'}).text.strip()

            writer.writerow([championship_name, teamA, score, teamB, time])
