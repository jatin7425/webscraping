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

