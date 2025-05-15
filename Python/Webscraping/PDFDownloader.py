import requests
from bs4 import BeautifulSoup
import os

folder_location = r'C:\webscraping'

# URL of the website to scrape
url = 'https://www.wanfried.de/rathaus/ehrungen-der-stadt-wanfried/'

# Send a GET request to the URL
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the webpage
links = soup.select("a[href$='.pdf']")

print(links)

i = 0

for link in links:
     if ('.pdf' in link.get('href', [])):
         print(link)


# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        i += 1
        print("Downloading file: ", i)
 
        # Get response object for link
        response = requests.get(link.get('href'))
        # Write content in pdf file
        pdf = open(filename, 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")
 
print("All PDF files downloaded")