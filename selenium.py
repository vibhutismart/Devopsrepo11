from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Path to the ChromeDriver executable
CHROME_DRIVER_PATH = '/var/lib/docker/volumes/jenkins_home/_data/final_project/roles/chromedriver'

# URL of your PHP website
URL = 'http://54.91.115.159:8089/'

# Initialize the Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't want a visible browser window
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the PHP website
    driver.get(URL)
    
    # Wait for the page to load
    time.sleep(2)  # Adjust time based on your page load time

    # Find the “About” link or button and click it
    about_button = driver.find_element(By.LINK_TEXT, 'About')  # Adjust if the selector is different
    about_button.click()

    # Wait for the page to load
    time.sleep(2)  # Adjust time based on your page load time

    # Verify the text on the page
    expected_text = 'This is the about page'  # Replace with the actual text you expect
    body_text = driver.find_element(By.TAG_NAME, 'body').text
    
    assert expected_text in body_text, f"Text '{expected_text}' not found in page content"

    print("Test passed: 'About' page contains the expected text.")
    
except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser
    driver.quit()

