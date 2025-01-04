# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument('--headless')  # Enable headless mode
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional)
# chrome_options.add_argument('--no-sandbox')  # This is sometimes required in certain environments

# # Set up the WebDriver with the options
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)

# # Open a website
# driver.get('https://www.google.com')

# # Perform actions
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('Selenium Headless')
# search_box.submit()

# # Close the browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

# Start Helper Functions
def setup_driver(user_agent=None):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode
    # chrome_options.add_argument("--no-sandbox")  # Required for headless mode on some systems
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    # chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    # chrome_options.add_argument("--disable-extensions")  # Disable extensions for performance
    # chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    # chrome_options.add_argument("--disable-notifications")  # Disable notifications
    # chrome_options.add_argument("--disable-infobars")  # Disable infobars
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation controlled
    # chrome_options.add_argument("--disable-web-security")  # Disable web security
    # chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")  # Disable isolate origins and site per process

    if user_agent:
        chrome_options.add_argument(f"user-agent={user_agent}")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_window_size(2048, 1536)
        return driver
    except:
        return None

driver = setup_driver()
driver.get('https://google.com')

# Perform actions
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Selenium Headless')
search_box.submit()

# Close the browser
driver.quit()