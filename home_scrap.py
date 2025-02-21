
from bs4 import BeautifulSoup
import csv
import requests
import random

url = "https://www.dell.com/support/home/en-in"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
]

headers = {
    "User-Agent": random.choice(user_agents),
    "Referer": "https://www.google.com/",
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_page(url, headers, path):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Page fetched successfully!")
        with open(path, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        print(f"Failed to fetch page: {response.status_code}")

fetch_page(url, headers, "data/home.html")

# Read the saved HTML file
with open("data/home.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all images
images = []
hyperlinks = []
buttons = []



for img in soup.find_all("img"):
    img_src = img.get("src")
    img_alt = img.get("alt", "No Alt Text")
    images.append({"src": img_src, "alt": img_alt})
    hyperlinks.append({"text" : f"{img_alt} image", "url": img_src})

# Find all hyperlinks
for link in soup.find_all("a"):
    link_text = link.text.strip() if link.text.strip() else "No Text"
    link_href = link.get("href")
    hyperlinks.append({"text": link_text, "url": link_href})

# Find all buttons (regular <button> tags)
for button in soup.find_all("button"):
    button_text = button.text.strip() if button.text.strip() else "No Text"
    buttons.append({"text": button_text})

# Find clickable divs (buttons disguised as <div> or <a> with a button class)
for div_button in soup.find_all(["div", "a"], class_=lambda x: x and "button" in x.lower()):
    button_text = div_button.text.strip() if div_button.text.strip() else "No Text"
    buttons.append({"text": button_text})



# Save to CSV files
def save_to_csv(filename, fieldnames, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

save_to_csv("data/images.csv", ["src", "alt"], images)
save_to_csv("data/links.csv", ["text", "url"], hyperlinks)
save_to_csv("data/buttons.csv", ["text"], buttons)

print("Data extraction completed! Images, links, and buttons saved to CSV.")

