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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Setup ChromeDriver path
CHROME_DRIVER_PATH = "chromedriver.exe"

# Initialize the WebDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

try:
    # Open a website (example: Google)
    driver.get("https://www.google.com")
    print("Website opened successfully")

    # Find the search input field
    search_box = driver.find_element(By.NAME, "q")
    search_query = "Selenium Python"

    # Enter search query and press Enter
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    print(f"Search performed for: {search_query}")

    # Wait for results to load
    time.sleep(2)

    # Scrape the search result titles
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    print("Search Results:")
    for index, result in enumerate(results[:10], start=1):  # Limit to first 10 results
        print(f"{index}. {result.text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

# # Start Helper Functions
# def setup_driver(user_agent=None):
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")  # Run in headless mode
#     # chrome_options.add_argument("--no-sandbox")  # Required for headless mode on some systems
#     # chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
#     # chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
#     # chrome_options.add_argument("--disable-extensions")  # Disable extensions for performance
#     # chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
#     # chrome_options.add_argument("--disable-notifications")  # Disable notifications
#     # chrome_options.add_argument("--disable-infobars")  # Disable infobars
#     # chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation controlled
#     # chrome_options.add_argument("--disable-web-security")  # Disable web security
#     # chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")  # Disable isolate origins and site per process

#     if user_agent:
#         chrome_options.add_argument(f"user-agent={user_agent}")
    
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         driver.set_window_size(2048, 1536)
#         return driver
#     except:
#         return None

# driver = setup_driver()
# driver.get('https://google.com')

# # Perform actions
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('Selenium Headless')
# search_box.submit()

# # Close the browser
# driver.quit()


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

from django.conf.urls.static import static
from django.conf import settings

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

AUTH_USER_MODEL = 'users.UserProfile'

from webapp.models import Records
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_user')

    context = {'form': form}
    return render(request, 'register.html', context=context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'user_login.html', context=context)

def logout_user(request):
    logout(request)
    messages.success(request, "Successful Signout.")
    return redirect('login_user')

@login_required(login_url='login_user/')
def dashboard(request):
    user_records = Records.objects.all()
    context = {'records': user_records}
    return render(request, 'dashboard.html', context=context)

@login_required(login_url='login_user/')
def create_record(request):
    form = AddRecordForm()

    if request.method == 'POST':
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'create_record.html', context=context)

@login_required(login_url='login_user/')
def update_record(request, pk):
    record = Records.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Successful Record Updated.")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'update_record.html', context=context)

@login_required(login_url='login_user/')
def delete_record(request, pk):
    delete_record = Records.objects.get(id=pk)
    delete_record.delete()
    return redirect('dashboard')

@login_required(login_url='login_user/')
def singular_record(request, pk):
    single_record = Records.objects.get(id=pk)
    context = {'record': single_record}
    return render(request, 'view-record.html', context=context)


{% if messages %}
    {% for message in messages %}
    <div class="alert alert-success d-flex align-items-center container" id="message_alert" role="alert">
        <i class="fa-solid fa-circle-check fa-lg m-2"></i> 
        <div class="message">
            {{ message }}
        </div>
    </div>
    {% endfor %}
{% endif %}


from django import forms
from webapp.models import Records
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Create User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Create a Record
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name', 'last_name' , 'email', 'phone', 'address', 'city', 'state', 'country']

# Update a Record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name', 'last_name' , 'email', 'phone', 'address', 'city', 'state', 'country']