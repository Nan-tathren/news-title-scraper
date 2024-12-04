# News Title Scraper

This is a Python-based scraper that collects news titles from "https://www.seznamzpravy.cz/sekce/stalo-se-177" and saves them into a PostgreSQL database.

## Project Overview
The project uses Python to scrape news articles from "https://www.seznamzpravy.cz/sekce/stalo-se-177", store the titles, and the timestamp of when they were scraped. The data is stored in a PostgreSQL database for easy querying and analysis.

## Features
- Scrapes news articles from seznamzpravy.cz.
- Saves titles and timestamps in a PostgreSQL database.
- Easy to extend to support more news sources.

## Technologies Used
- **Python**: The main programming language used for the scraper.
- **PostgreSQL**: For storing the scraped data.
- **BeautifulSoup & Requests**: For scraping news websites.

## Installation Instructions

### Prerequisites
- Python 3.x
- PostgreSQL
- Required Python libraries (listed in `requirements.txt`)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Nan-tathren/news-title-scraper.git

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
