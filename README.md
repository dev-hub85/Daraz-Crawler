# 🕷️ Daraz Products Crawler

> A powerful web crawler to scrape product listings across all categories and sub-categories on the Daraz marketplace.

---

## 📦 Overview

The **`categories.json`** file contains the full hierarchy of Daraz categories — including **main categories**, **nested categories**, and **sub-categories** — used to guide the crawler across the entire site.

---

## ⚙️ Setup & Installation

### 1. Create a Virtual Environment

```bash
python -m venv ecom_crawler
```

### 2. Activate the Virtual Environment

**macOS / Linux:**
```bash
source ecom_crawler/bin/activate
```

**Windows:**
```bash
ecom_crawler\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install pymongo scrapy ipython
```

| Package     | Purpose                              |
|-------------|--------------------------------------|
| `scrapy`    | Core web crawling framework          |
| `pymongo`   | MongoDB integration for data storage |
| `ipython`   | Enhanced interactive Python shell    |

---

## 🚀 Running the Crawler

### 4. Navigate into the Project Directory

```bash
cd ecom_crawler
```

### 5. Start the Spider

```bash
scrapy crawl ecomspider
```

---

## 📁 Project Structure

```
ecom_crawler/
├── ecom_crawler/
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── ecomspider.py     # Main spider logic
│   ├── __init__.py
│   ├── items.py              # Scrapy item definitions
│   ├── middlewares.py        # Custom middlewares
│   ├── pipelines.py          # Data pipelines (MongoDB)
│   └── settings.py           # Scrapy settings & config
├── .gitattributes
├── categories.json           # Full Daraz category hierarchy
├── data2.json                # Crawled output data
├── itmedata.json             # Crawled item detail data
├── README.md
└── scrapy.cfg                # Scrapy project configuration
```

---

## 📌 Notes

- Make sure **MongoDB** is running locally before starting the crawler if using the `pymongo` pipeline.
- The crawler traverses **all sub-categories** defined in `categories.json` automatically.
- For large crawls, consider configuring rate limits in `settings.py` to avoid getting blocked.

---

> **Tip:** Run `scrapy check ecomspider` to validate your spider before a full crawl.
