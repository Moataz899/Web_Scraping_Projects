from bs4 import BeautifulSoup
import csv

with open('D:\\Abdelraouf\\Web_Scraping_Projects\\Web_Scraping_Projects\\Projects\\Project_3\\index.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    
    course_cards = soup.find_all('div', class_='card')
    
    with open('courses.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Course Name', 'Course Price', 'Course Description'])
        
        for course_card in course_cards:
            course_name = course_card.find('h5').text
            course_price = course_card.find('a', class_='btn btn-primary').text
            course_description = course_card.find('p').text
            
            csv_writer.writerow([course_name, course_price, course_description])
