import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
from selenium import webdriver

# Basic Web Scraping Example
def basic_scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Print prettified HTML
    print(soup.prettify())

    # Extract the title of the webpage
    title = soup.title
    print("Title:", title.text)
    
    # Find all links on the page
    links = soup.find_all('a')
    print("\nLinks found:")
    for link in links:
        print(link.get('href'))

# Navigating HTML Tree
def navigate_html_tree(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find first paragraph and next sibling
    first_paragraph = soup.find('p')
    print("First paragraph:", first_paragraph.text)
    sibling = first_paragraph.find_next_sibling('p')
    print("Next sibling:", sibling.text)

# Extract Data from Tables
def extract_table_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the first table
    table = soup.find('table')
    
    # Extract all rows from the table
    rows = table.find_all('tr')
    print("\nTable data:")
    for row in rows:
        cols = row.find_all('td')
        cols_text = [col.text.strip() for col in cols]
        print(cols_text)

# Handle Pagination
def handle_pagination(base_url, start_page, end_page):
    for page_num in range(start_page, end_page + 1):
        url = f'{base_url}{page_num}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract all titles
        titles = soup.find_all('h2')
        print(f"\nPage {page_num} Titles:")
        for title in titles:
            print(title.text)

# Handle Forms
def handle_forms(url):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    form = soup.find('form')
    inputs = form.find_all('input')
    
    # Prepare data for form submission
    form_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
    }
    
    # Submit the form
    post_url = form.get('action')
    response = session.post(post_url, data=form_data)
    print("\nForm submission response:")
    print(response.text)

# Store Data in CSV File
def store_data_csv():
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'San Francisco'],
    ]
    
    # Write to CSV
    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("\nData has been written to data.csv.")

# Store Data in SQLite Database
def store_data_sqlite():
    # Create a new SQLite database (or connect if it exists)
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    ''')

    # Insert data into the table
    cursor.execute('''
        INSERT INTO users (name, age, city) VALUES (?, ?, ?)
    ''', ('Alice', 30, 'New York'))

    # Commit and close
    conn.commit()
    conn.close()
    print("\nData has been inserted into the SQLite database.")

# Error Handling in Requests
def error_handling(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        print("\nPage content retrieved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Handling JavaScript-rendered pages with Selenium
def scrape_dynamic_content(url):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Change the path to your driver
    driver.get(url)

    # Wait for JavaScript to render the content
    driver.implicitly_wait(5)

    # Get the page content and parse it with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Example: Extract all paragraphs
    paragraphs = soup.find_all('p')
    print("\nParagraphs from dynamic content:")
    for para in paragraphs:
        print(para.text)

    driver.quit()  # Close the browser window

if __name__ == "__main__":
    # Basic Scraping
    basic_scraping('https://example.com')

    # Navigate HTML Tree
    navigate_html_tree('https://example.com')

    # Extract Data from Table
    extract_table_data('https://example.com')

    # Handle Pagination
    handle_pagination('https://example.com/page/', 1, 3)

    # Handle Forms (ensure to change the URL for a real form)
    handle_forms('https://example.com/form')

    # Store Data in CSV
    store_data_csv()

    # Store Data in SQLite
    store_data_sqlite()

    # Error Handling
    error_handling('https://example.com')

    # Scrape Dynamic Content using Selenium
    scrape_dynamic_content('https://example.com')
