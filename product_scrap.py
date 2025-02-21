import requests
from bs4 import BeautifulSoup
import json
import random
import re

# Dell Product Page URL
URL = "https://www.dell.com/en-in/shop/laptop-notebook-computers/vostro-3520-laptop/spd/vostro-15-3520-laptop/vn3520vmn67001sdb1?ref=variantstack"

# User-Agent to simulate a browser request
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

# Send GET request

def extract_base_url(image_url):
    """
    Extracts the base URL from a Dell image URL by removing query parameters.

    :param image_url: A single image URL (string)
    :return: Base URL (string)
    """
    return image_url.split("?")[0] if "?" in image_url else image_url

def main(URL, headers):
    response = requests.get(URL, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch page: {response.status_code}")
    else:
        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product title
        product_title = soup.find("h1")
        product_title = product_title.text.strip() if product_title else "N/A"

        # Extract product price
        price_container = soup.find("span", class_="sale-price")
        product_price = price_container.text.strip() if price_container else "N/A"

        # Extract images from figure elements
        li = soup.find_all("li", class_="active-group")
        
        image_urls = []
        for li in li:

            img_tag = li.find("img")
            if not img_tag:
                print("❌ Image not found in this <li>")
                continue  # Skip to next <li>
            
            # Extract the image URL (check both 'src' and 'data-src')
            img_url = img_tag.get("src") if img_tag.get("src").startswith("//") else img_tag.get("data-src")

            if img_url and not img_url.startswith("data:image"):  # Avoid placeholder images
                img_url = "https:" + img_url if img_url.startswith("//") else img_url  # Ensure full URL
                refined_url = extract_base_url(img_url)  # Remove query params

                image_urls.append({
                    "name": img_tag.get("alt", "No Alt"),  # Use alt text or fallback
                    "src": refined_url
                })
        # Save extracted data to JSON
        product_data = {
            "title": product_title,
            "price": product_price,
            "images": image_urls,
            "product_url": URL
        }

        # Save to JSON file
        with open(f"product/{product_data["title"]} details.json", "w", encoding="utf-8") as f:
            json.dump(product_data, f, indent=4)

        print("\n✅ Product Data Extracted:\n", json.dumps(product_data, indent=4))

main(URL, headers)