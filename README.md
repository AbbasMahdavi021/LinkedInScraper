# LinkedIn Post Comments Scraper

A Python script using Selenium to scrape comments from a LinkedIn post.

It allows scraping of all comments if authenticated or public comments otherwise.

## Introduction

This project provides a Python script (`main.py`) that utilizes Selenium to scrape comments from a LinkedIn post.

It includes functionality for handling authentication, obtaining the post URL, and scraping comments either in authenticated mode or public mode.

## Features

- Scrape comments from a LinkedIn post using Selenium.
- Handle authentication prompts if required.
- Scrape all comments if authenticated; otherwise, scrape public comments only.
- Save scraped data to CSV format.

## Requirements

- Python
- Chrome WebDriver, default provided.

  (Download from [Chrome Driver Downloads](https://chromedriver.chromium.org/downloads))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LinkedIn-Post-Comments-Scraper.git
   ```
2. The project comes with a default Chrome WebDriver (chromedriver.exe) located in the ./drivers/ directory.
   If this version is compatible with your system, no further action is needed.

   Note: If the default WebDriver is not compatible with your system or Chrome version, you can download the appropriate WebDriver from Chrome Driver Downloads and replace the existing chromedriver.exe in the ./drivers/ directory.

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory.
2. Run the script:
   ```
   python main.py
   ```
3. Follow authentication prompts if required.
4. Provide the URL of the LinkedIn post when prompted.
5. The script will scrape comments based on authentication status and save the data to a CSV file.
6. The browser window will remain open after execution.
