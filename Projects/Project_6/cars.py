from bs4 import BeautifulSoup
import requests
import csv

cars = []
for i in range(1, 101):
    url = f"https://eg.hatla2ee.com/en/car/page/{i}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ul = soup.find('div', class_='CarListWrapper')
        if ul:
            models = ul.find_all('div', class_='newCarListUnit_contain newPDealUnit')
            for model in models:
                image = model.find('img')['src']
                title = model.find('div', class_='newCarListUnit_header').text.strip()
                price = model.find('div', class_='main_price').text.strip()
                date = model.find('div', class_='otherData_Date').text.strip()
                cars.append([title, price, date, image])
    else:
        print(f"Failed to retrieve page {i}")

with open('cars.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Date', 'Image'])
    writer.writerows(cars)

print('CSV file created successfully.')
