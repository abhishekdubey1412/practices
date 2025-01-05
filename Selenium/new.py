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