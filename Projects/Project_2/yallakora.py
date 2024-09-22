import requests
from bs4 import BeautifulSoup
import csv

date = input("Please Enter A Date In Format MM/DD/YYYY: ")
page = requests.get(f"http://www.yallakora.com//Match-Center/?date={date}")

def main(page):
    
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []
    
    championships = soup.find_all("div", {'class': 'matchCard'})
    print(f"Found {len(championships)} championships")

    def get_match_info(championships):
        
        championship_title = championships.contents[1].find("h2").text.strip()  
        all_matches = championships.contents[3].find_all('li')
        number_of_matches = len(all_matches)
        print(f"Found {number_of_matches} matches in {championship_title}")
        
        for i in range(number_of_matches):   # get Teams Names
            team_A = all_matches[i].find("div", {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find("div", {'class': 'teamB'}).text.strip()

            # get score
            match_result = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            
            # get time
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'time'}).text.strip()
            
            # add match info to matches _details
            matches_details.append({
                "Championship": championship_title,
                "Team A": team_A,
                "Team B": team_B,
                "Score": score,
                "Time": match_time
            })
    for i in range(len(championships)):
        get_match_info(championships[i])

    print(f"Total matches found: {len(matches_details)}")
    if matches_details:
        keys = matches_details[0].keys()
        with open('D:/Abdelraouf/Web_Scraping_Projects/Web_Scraping_Projects/Projects/Project_2/matches-deatils.csv', 'w') as ouput_file:
            dict_writer = csv.DictWriter(ouput_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_details)
            print("File Created")
    else:
        print("No match details found for the given date.")

main(page)
