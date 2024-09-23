from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

with open('jobs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Required Skills', 'More Info'])

    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:  # Check if the job was posted recently
            company_name = job.find('h3', class_='joblist-comp-name').text.strip().replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.strip().replace(' ', '')
            more_info = job.header.h2.a['href']

            print(f"Company Name: {company_name}")
            print(f"Required Skills: {skills}")
            print(f"More Info: {more_info}")
            print(' ')

            writer.writerow([company_name, skills, more_info])
