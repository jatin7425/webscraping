# 🖥️ Dell Product & Support Page Scraper

## 🚀 Overview
This project includes web scrapers designed to extract product details and support page data from [Dell's website](https://www.dell.com). The extracted data is saved in structured formats for further analysis and automation.

---

## 📌 Scripts & Workflow

### **1️⃣ Product Scraper (`all_product_scrap.py`)**
This script extracts product data from multiple Dell product categories, including laptops, desktops, monitors, and accessories.

#### **🔄 Workflow:**
1. **Fetch Product Pages**
   - Iterates through different product categories.
   - Sends requests to Dell's website using randomized User-Agent headers.
   - Saves raw HTML pages in `webpage_templates/{category}/`.

2. **Extract Product Details**
   - Parses stored HTML files with BeautifulSoup.
   - Extracts product details including:
     - 🏷️ **Name**
     - 💰 **Price**
     - 🖼️ **Image URLs** (primary & secondary images)
     - 🔗 **Product Link**
     - ⭐ **Ratings**
     - 🔹 **Features** (for laptops, desktops, etc.)
     - 📝 **Specifications** (for monitors, audio, and accessories)
   - Stores extracted data in `data/details.json`.

---

### **2️⃣ Dell Support Page Scraper (`home_scrap.py`)**
This script extracts images, hyperlinks, and buttons from the Dell Support page.

#### **🔄 Workflow:**
1. **Fetch the Support Page**
   - Sends a request to the Dell Support page.
   - Saves HTML content in `webpage_templates/pages/home.html`.

2. **Extract Relevant Data**
   - Parses the HTML to extract:
     - 🖼️ **Images** (`src` and `alt` attributes)
     - 🔗 **Hyperlinks** (`a` tags including text and URLs)
     - 🎛️ **Buttons** (`<button>` tags and elements styled as buttons, including clickable `div` and `a` elements)

3. **Save Extracted Data to CSV**
   - 📂 **Images** → `data/images.csv`
   - 📂 **Links** → `data/links.csv`
   - 📂 **Buttons** → `data/buttons.csv`

---

## ⚙️ Prerequisites
- 🐍 Python 3.x
- Install dependencies:
  - For Ubuntu/Linux: `pip install -r requirements.txt`
  - For Windows: `pip install -r win-requirements.txt`

---

## 📥 Installation & Usage

1️⃣ Clone the repository:
```sh
 git clone https://github.com/jatin7425/webscraping.git
 cd webscraping
```

2️⃣ Create & activate a virtual environment (optional but recommended).

3️⃣ Install dependencies:
```sh
 pip install -r requirements.txt  # Ubuntu/Linux
 pip install -r win-requirements.txt  # Windows
```

4️⃣ Run the scrapers:
```sh
 python all_product_scrap.py  # Scrape product data
 python home_scrap.py  # Scrape support page data
```

---

## 📊 Sample Output

### **📦 Product Scraper (`data/details.json`):**
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

### **🖼️ Support Page Scraper Output:**

📂 **images.csv:**
```
src,alt
https://example.com/image1.jpg,Support Logo
https://example.com/image2.jpg,No Alt Text
```

📂 **links.csv:**
```
text,url
Support Page,https://www.dell.com/support
Contact Us,https://www.dell.com/contact
```

📂 **buttons.csv:**
```
text
Submit
Learn More
```

