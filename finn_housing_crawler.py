from bs4 import BeautifulSoup
import requests

# Define the URL of the site
base_url = "https://www.finn.no/realestate/homes/search.html?location=0.20061&sort=PUBLISHED_DESC"

# Send HTTP request to the specified URL and save the response from server in a response object called r
r = requests.get(base_url)

# Create a BeautifulSoup object and specify the parser library at the same time
soup = BeautifulSoup(r.text, "html.parser")

# Find all links on the page (limit to the first 5 for the purpose of this example)
area_h3_tag = soup.find("h3", string="Område")
next_element = area_h3_tag.find_next_sibling()

# Find all 'li' children of the 'ul' tag
list_items = next_element.find_all("li")
area_dict = {}
for li_area in list_items:
    div = li_area.find("div")
    check_box = div.find("input")
    label = div.find("label")
    span = label.find("span")

    oslo_area = label.contents[0].strip()
    location = label["for"].replace("location-", "")
    span_number = int(span.get_text().strip("()").replace("\xa0", "").strip())
    area_dict[oslo_area] = {"location": location, "num": span_number}
