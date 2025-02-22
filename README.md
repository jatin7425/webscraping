# Web Scraping Project

This repository contains scripts for scraping product data from Dell's website. The scraped data is stored in JSON format.

## Features
- Scrapes product details from multiple categories.
- Stores scraped data in JSON format.
- Provides separate dependency files for Windows and Ubuntu.

## Repository Structure
```
webscraping/
│-- .gitignore
│-- all_product_scrap.py  # Script to scrape all products
│-- home_scrap.py         # Script to scrape home page data
│-- requirements.txt      # Dependencies for Ubuntu/Linux
│-- win-requirements.txt  # Dependencies for Windows
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/jatin7425/webscraping.git
cd webscraping
```

### 2. Install Dependencies
#### On Ubuntu/Linux:
```sh
pip install -r requirements.txt
```
#### On Windows:
```sh
pip install -r win-requirements.txt
```

### 3. Run the Scraper
To scrape product data, use:
```sh
python all_product_scrap.py
```

To scrape home page data, use:
```sh
python home_scrap.py
```


# this repo include two file



# Web Scraper for Dell Support Page

## Overview

This project is a web scraper that extracts images, hyperlinks, and buttons from the [Dell Support Page](https://www.dell.com/support/home/en-in). The extracted data is saved into structured CSV files for further analysis and automation.

## Workflow

1. **Fetch the Web Page**
   - Sends a request to the Dell Support page.
   - Uses random User-Agent headers to avoid detection.
   - Saves the HTML content to `webpage_templates/pages/home.html`.

2. **Parse the HTML**
   - Uses BeautifulSoup to parse the downloaded HTML file.
   - Extracts:
     - **Images** (`src` and `alt` attributes)
     - **Hyperlinks** (`a` tags including text and URLs)
     - **Buttons** (`<button>` tags and elements styled as buttons, including clickable `div` and `a` elements)

3. **Save Extracted Data to CSV**
   - Saves extracted images to `data/images.csv`
   - Saves extracted links to `data/links.csv`
   - Saves extracted buttons to `data/buttons.csv`

## Prerequisites

- Python 3.x
- Install required dependencies using `pip install -r requirements.txt`

## Installation & Usage

1. Clone the repository and navigate to the project folder.
2. Create a virtual environment (optional but recommended) and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the scraper script.

## Sample Output

The extracted data is saved in CSV format. Example structure:

**images.csv:**
```
src,alt
https://example.com/image1.jpg,Product Image
https://example.com/image2.jpg,No Alt Text
```

**links.csv:**
```
text,url
Support Page,https://www.dell.com/support
Contact Us,https://www.dell.com/contact
```

**buttons.csv:**
```
text
Submit
Learn More
```


# Web Scraper for Dell Product Pages

## Overview

This project includes web scrapers designed to extract product details and support page data from [Dell's website](https://www.dell.com). The extracted data is saved in structured formats for further analysis and automation.

## Scripts & Workflow

### **1. Product Scraper (`all_product_scrap.py`)**

This script extracts product data from multiple Dell product categories, including laptops, desktops, monitors, and accessories.

#### **Workflow:**
1. **Fetch Product Pages**
   - Iterates through different product categories.
   - Sends requests to Dell's website using randomized User-Agent headers.
   - Saves raw HTML pages in `webpage_templates/{category}/`.

2. **Extract Product Details**
   - Parses stored HTML files with BeautifulSoup.
   - Extracts product details including:
     - **Name**
     - **Price**
     - **Image URLs** (primary & secondary images)
     - **Product Link**
     - **Ratings**
     - **Features** (for laptops, desktops, etc.)
     - **Specifications** (for monitors, audio, and accessories)
   - Stores extracted data in `data/details.json`.

### **2. Dell Support Page Scraper (`home_scrap.py`)**

This script extracts images, hyperlinks, and buttons from the Dell Support page.

#### **Workflow:**
1. **Fetch the Support Page**
   - Sends a request to the Dell Support page.
   - Saves HTML content in `webpage_templates/pages/home.html`.

2. **Extract Relevant Data**
   - Parses the HTML to extract:
     - **Images** (`src` and `alt` attributes)
     - **Hyperlinks** (`a` tags including text and URLs)
     - **Buttons** (`<button>` tags and elements styled as buttons, including clickable `div` and `a` elements)

3. **Save Extracted Data to CSV**
   - Saves extracted images to `data/images.csv`
   - Saves extracted links to `data/links.csv`
   - Saves extracted buttons to `data/buttons.csv`

## Prerequisites

- Python 3.x
- Install dependencies using `pip install -r requirements.txt` (for Ubuntu) or `pip install -r win-requirements.txt` (for Windows).

## Installation & Usage

1. Clone the repository and navigate to the project folder.
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies.
4. Run the scrapers to extract and store data.

## Sample Output

**Product Scraper (`data/details.json`):**
```json
[
    {
        "Product_Type": "laptop",
        "name": "Dell XPS 15",
        "price": "₹1,50,000",
        "image": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
        "link": "https://www.dell.com/xps-15",
        "ratings": "4.5 stars",
        "features": ["Intel i7", "16GB RAM", "512GB SSD"]
    }
]
```

**Support Page Scraper Output:**

**images.csv:**
```
src,alt
https://example.com/image1.jpg,Support Logo
https://example.com/image2.jpg,No Alt Text
```

**links.csv:**
```
text,url
Support Page,https://www.dell.com/support
Contact Us,https://www.dell.com/contact
```

**buttons.csv:**
```
text
Submit
Learn More
```



