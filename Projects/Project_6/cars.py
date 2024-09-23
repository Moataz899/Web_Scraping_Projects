from bs4 import BeautifulSoup
import requests
import csv

cars = []

for i in range(1, 20):
    url = f"https://eg.hatla2ee.com/en/car/page/{i}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {i}. Status code: {response.status_code}")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')
    ul = soup.find('div', class_='CarListWrapper')
    
    if ul is None:
        print(f"No car listings found on page {i}.")
        continue
    
    models = ul.find_all('div', class_='newCarListUnit_contain newPDealUnit')

    for model in models:
        image = model.find('img')['src'] if model.find('img') else 'No Image'
        title = model.find('div', class_='newCarListUnit_header').get_text(strip=True) if model.find('div', class_='newCarListUnit_header') else 'No Title'
        price = model.find('div', class_='main_price').get_text(strip=True) if model.find('div', class_='main_price') else 'No Price'
        date = model.find('div', class_='otherData_Date').get_text(strip=True) if model.find('div', class_='otherData_Date') else 'No Date'

        cars.append([title, price, date, image])

with open('cars.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Date', 'Image'])
    writer.writerows(cars)

print('CSV file created successfully.')
