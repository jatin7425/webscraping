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

