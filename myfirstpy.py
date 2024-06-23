import requests
from bs4 import BeautifulSoup
import csv

# Replace with the actual URL of the internal website you want to scrape
url = 'https://example-internal-website.com'

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data you want to scrape. Here's an example of scraping all rows from a table with the id 'data-table'
    table = soup.find('table', {'id': 'data-table'})
    rows = table.find_all('tr') if table else []

    # Extract the text from each row's columns (assuming each row has the same number of columns)
    scraped_data = [
        [td.text.strip() for td in row.find_all('td')]
        for row in rows if row.find_all('td')
    ]

    # Define the CSV file name where the data will be saved
    csv_file = 'scraped_data.csv'

    # Open the CSV file in write mode
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the headers (if the table has headers)
        headers = [th.text.strip() for th in rows[0].find_all('th')] if rows[0].find_all('th') else []
        if headers:
            writer.writerow(headers)

        # Write the data rows to the CSV file
        for data_row in scraped_data:
            writer.writerow(data_row)

    print(f'Data scraped and saved to {csv_file}')
else:
    print(f'Failed to retrieve data from the website. Status code: {response.status_code}')
