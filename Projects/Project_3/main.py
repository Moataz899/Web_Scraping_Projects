from bs4 import BeautifulSoup

with open('D:\Abdelraouf\Web_Scraping_Projects\Web_Scraping_Projects\Projects\Project_3\index.html', 'r') as html_file:
    content = html_file.read()
    # print(content) #print the content of file html
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify()) #print The Content Of File 
    
    courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags) # Print All Tags That Have H5
    # for course in courses_html_tags:
    #      print(course.text) # Print All Courses Name
    
    phrase_html_tags = soup.find_all('p')    
    # for p in phrase_html_tags:
    #      print(p.text) # Print all Phrases Of Content
    
    price_html_tags = soup.find_all('a', class_ ='btn btn-primary')
    # for p in price_html_tags:
    #     print(p.text) # Print All Price Of Courses
    
    course_cards = soup.find_all('div', class_ = 'card')
    
    for course_card in course_cards:
        course_name = course_card.find('h5').text
        course_price = course_card.find('a', class_ ='btn btn-primary').text
        course_description = course_card.find('p').text
        
        print(f'Course Name: {course_name}')
        print(f'Course Price: {course_price}')
        print(f'Course Description: {course_description}')
        print('---' * 10)