import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://www.cnn.com'

# Send an HTTP request to fetch the webpage content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

# Extract relevant data (modify this part according to your needs)
# Example: Extract all <p> tags
paragraphs = soup.find_all('div')

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Text': [div.get_text() for div in paragraphs]})

# Save the data to a CSV file
csv_filename = 'webpage_data.csv'
df.to_csv(csv_filename, index=False)

print(f'Data saved to {csv_filename}')
