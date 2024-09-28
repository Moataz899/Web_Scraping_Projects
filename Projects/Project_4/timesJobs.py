from bs4 import BeautifulSoup
import requests
import csv

csvfile = open('TimesJobs.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csvfile)
writer.writerow(['Job Title', 'Company Name', 'Skills'])

for i in range(10):
    url = f"https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=ai%20engineer&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=ai%20engineer&searchBy=0&rdoOperator=OR&pDate=I&sequence=2&startPage={i}"
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'html.parser')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        job_title = job.find('a').text.strip()
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        
        writer.writerow([job_title, company_name, skills])
        
csvfile.close()
