from bs4 import BeautifulSoup
import requests
import csv 

csvfile = open('wuzzuf_jobs.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csvfile)
writer.writerow(["Job Title", "Company", "Location", "Job Type"])

for i in range(4):
    url = f"https://wuzzuf.net/search/jobs/?a=hpb&q=ai%20engineer&start={i}"
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'html.parser')
    jobs = soup.find_all('div', class_='css-pkv5jc')

    for job in jobs:
        job_title = job.find('a', class_='css-o171kl').text
        company = job.find('a', class_='css-17s97q8').text
        location = job.find('span', class_='css-5wys0k').text
        job_type = job.find('span', class_='css-1ve4b75 eoyjyou0').text
        
        writer.writerow([job_title, company, location, job_type])

csvfile.close()

