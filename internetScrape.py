import requests
from bs4 import BeautifulSoup

# Set the URL to scrape
url = "https://www.google.com/search?q="

inputtext = input("Who do you wanna look up? ")

newt = inputtext.replace(" ", "+")

# Make a request to the URL and retrieve the HTML
html = requests.get(url+newt).content
print(url+newt)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the elements with the class "r" (these are the search results)
results = soup.find_all("a")

# Open the output file for writing
with open(inputtext + ".txt", "w") as outfile:
    # Loop through the results and write each one to the output file
    for link in results:
        if ("http" in link.get('href')[0:4]):
            # removes links that aren't needed 
            if ("https://support.google.com" in link.get('href')[0:27]):
                ""
            elif ("https://accounts.google.com" in link.get('href')[0:28]):
                ""
            elif ("https://policies.google.com" in link.get('href')[0:28]):
                ""
            else:
                outfile.write(link.get('href') + "\n")
        elif ("/url?q" in link.get('href')[0:6]):
            outfile.write(link.get('href')[7:len(link.get('href'))] + "\n")