#  News Headline Scraper

A simple Python script that scrapes the latest top headlines from **NDTV News** using `requests` and `BeautifulSoup`, and saves them to a `.txt` file.

---

##  Objective

- Scrape top news headlines from a live website.
- Use Python tools like `requests` and `BeautifulSoup` for web scraping.
- Save the headlines in a plain text file for later use or analysis.

---

##  Tools Used

- **Python 3**
- [`requests`](https://pypi.org/project/requests/) — To fetch the webpage
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) — To parse HTML

---

##  Project Structure 
<pre> <code> news_project/ 
   ├── news_scraper.py # Main Python script to scrape headlines 
   ├── headlines.txt  
   └── README.md # Project documentation </code> </pre>


---

##  How to Run

1. **Install the required libraries** (if not already installed):

   ```bash
   pip install requests beautifulsoup4
   python news_project.py




