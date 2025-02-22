import json
import os
import random
import requests
import re
from bs4 import BeautifulSoup

urls = {
    "laptop": {"url": "https://www.dell.com/en-in/shop/dell-laptops/scr/laptops", "page_limit": 3},
    "desktop": {"url": "https://www.dell.com/en-in/shop/scc/scr/desktops", "page_limit": 1},
    "monitor": {"url": "https://www.dell.com/en-in/shop/all-monitors/sac/monitors/all-monitors", "page_limit": 8},
    "audio": {"url": "https://www.dell.com/en-in/shop/audio/ar/8310", "page_limit": 2},
    "cables-hubs-adapters": {"url": "https://www.dell.com/en-in/shop/cables-hubs-adapters/ar/8167", "page_limit": 16},
    "storage-drives-media": {"url": "https://www.dell.com/en-in/shop/storage-drives-media/ar/5683", "page_limit": 24},
}


# MAX_PAGES = 40

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

def extract_base_url(image_url):
    """
    Extracts the base URL from a Dell image URL by removing query parameters.

    :param image_url: A single image URL (string)
    :return: Base URL (string)
    """
    return image_url.split("?")[0] if "?" in image_url else image_url


def sanitize_filename(category, page_number):
    """ Creates a valid filename for each page. """
    return f"webpage_templates/{category}/page_{page_number}.html"


def fetch_and_save_html(url, category, MAX_PAGES):
    """ Fetch all paginated pages until no more products exist. """
    os.makedirs(f"webpage_templates/{category}", exist_ok=True)

    for page in range(1, MAX_PAGES + 1):
        paginated_url = f"{url}?page={page}"
        response = requests.get(paginated_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        if response.status_code != 200:
            print(f"Stopping at page {page} for {category}, status: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("article", class_="ps-stack")

        if not products:
            print(f"No products found on page {page}. Stopping pagination.")
            break

        filename = sanitize_filename(category, page)
        with open(filename, "w", encoding="utf-8") as file:
            for product in products:
                file.write(str(product) + "\n\n")

        print(f"✅ Saved: {filename}")

# Fetch product pages
for category, data in urls.items():
    fetch_and_save_html(data['url'], category, data['page_limit'])



# Fetch Saved files
files_path = []

def list_directory_tree(root_dir):
    """Recursively lists only HTML files in a tree structure."""
    if not os.path.exists(root_dir):
        print("Directory does not exist!")
        return

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):  # Only save HTML files
                
                files_path.append(os.path.join(root, file))

root_directory = "webpage_templates"
list_directory_tree(root_directory)



# Read and extract product details from saved files
def extract_product_data(file_path):
    file_path = os.path.normpath(file_path)  # Normalize path for cross-platform compatibility
    path_parts = file_path.split(os.sep)  # Split the path into parts
    category_name = path_parts[1] if len(path_parts) > 1 else "unknown"  # Extract category safely
    
    """Reads an HTML file and extracts product names, price, image, and link."""
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        products = soup.find_all("article", class_="ps-stack")

        extracted_products = []
        for product in products:
            data_attr = product.get("data-product-detail")
            ratings = product.find_all("span", class_="ratings-off-screen")
            extracted_features = product.find_all("div", class_="key-feature-item")
            ps_iconography_specs_title = product.find_all("span", class_="ps-iconography-specs-title")
            ps_iconography_specs_label = product.find_all("span", class_="ps-iconography-specs-label")
            
            product_imgs = product.find("nav", class_="media-thumbs-mfe")
            secondary_imgs = []
            if product_imgs:
                # print(str(product_imgs)+"\n\n")
                product_img = product_imgs.find_all("img")
                for img in product_img:
                    img_src = "https:"+img.get("src", "N/A")
                    secondary_imgs.append(extract_base_url(img_src))
            
            # Extract features properly
            specs = [
                {"label": label.text.strip(), "value": value.text.strip()}
                for label, value in zip(ps_iconography_specs_title, ps_iconography_specs_label)
                if label and value
            ]
            list_features = [feature.find("span").text.strip() for feature in extracted_features if feature.find("span")]

            if not data_attr:
                continue
            
            try:
                product_json = json.loads(data_attr)
                product_info = list(product_json.values())[0]
                
                monitor_audio_product_data = {
                    "Product_Type": category_name,
                    "name": product_info.get("title", "Unknown Product"),
                    "price": product_info.get("dellPrice", "Unknown Price"),
                    "image": "https:" + product_info.get("image", ""),
                    "link": "https:" + product_info.get("pdUrl", "#"),
                    "ratings": ratings[0].text.strip() if ratings else "No Rating",
                    "specs": specs if specs else "No Spec",
                }
                
                product_data = {
                    "Product_Type": category_name,
                    "name": product_info.get("title", "Unknown Product"),
                    "price": product_info.get("dellPrice", "Unknown Price"),
                    "image": secondary_imgs,
                    "link": "https:" + product_info.get("pdUrl", "#"),
                    "ratings": ratings[0].text.strip() if ratings else "No Rating",
                    "features": list_features,
                }
                
                if category_name == "monitor" or category_name == "audio" or category_name == "cables-hubs-adapters" or category_name == "storage-drives-media":
                    extracted_products.append(monitor_audio_product_data)
                else:
                    extracted_products.append(product_data)
                    
            except json.JSONDecodeError:
                print(f"Error decoding JSON in {file_path}")

        return extracted_products




# Extract products from saved HTML files
all_products = []

for file_path in files_path:
    all_products.extend(extract_product_data(file_path))  # Add all extracted products
    
os.makedirs(f"data/", exist_ok=True)

# Save to JSON file properly
json_file = "data/details.json"

# Check if file exists, and load old data if present
if os.path.exists(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            old_data = json.load(f)
        except json.JSONDecodeError:
            old_data = []  # If file is corrupted, start fresh
else:
    old_data = []

# Merge old and new data
all_products.extend(old_data)

# Save back to JSON file properly
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(all_products, f, indent=4)

print(f"Extracted {len(all_products)} products and saved to {json_file}.")