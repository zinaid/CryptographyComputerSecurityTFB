import requests
from bs4 import BeautifulSoup
import csv

# Fetch web content
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Check if a tag exists before accessing it
if soup.h1:
    print(soup.h1.text)
else:
    print("No 'h1' tag found.")


# Find all headlines (h3 tags)
headlines = soup.find_all('h3')
for headline in headlines:
    print(headline.text)

# Find all elements with class "product_pod"
product_pods = soup.find_all('article', class_='product_pod')
# Create a CSV file and write the data
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Name', 'Price'])  # Write header row
    
    # Iterate through each product_pod and extract the name and price
    for product_pod in product_pods:
        # Find the element with class "price_color" inside the product_pod
        price_element = product_pod.find('p', class_='price_color')
        if price_element:
            price = price_element.text
            
            # Find the element with the product name
            name_element = product_pod.find('h3').find('a')
            if name_element:
                name = name_element.text.strip()
                csv_writer.writerow([name, price])  # Write data to CSV