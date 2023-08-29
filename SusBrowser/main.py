from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from faker import Faker


# Set up the browser for the bot to testing reCaptcha v3
# must lowest trust point
option = Options()

option.add_argument("--disable-infobars") 
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option = webdriver.ChromeOptions() 
option.add_argument(" — incognito")

# sproff as a bot
option.add_experimental_option("excludeSwitches", ["enable-automation"]) 
option.add_experimental_option('useAutomationExtension', False)

option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')
option.add_argument('--ignore-certificate-errors')
option.add_argument('--allow-running-insecure-content')
option.add_argument('--disable-web-security')
option.add_argument('--disable-client-side-phishing-detection')
option.add_argument('--disable-notifications')
option.add_argument('--disable-default-apps')
option.add_argument('--disable-crash-reporter')


# Open the browser
drive = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# Open the website
url = 'https://0a30-118-70-177-23.ngrok-free.app/lien-he/khieu-nai/'
# open the website 
drive.get(url)
# add ngrok-skip-browser-warning to header
drive.add_cookie({'name': 'ngrok-skip-browser-warning', 'value': 'true'})
# wait for load
drive.implicitly_wait(10)
# raise v3 reCaptcha low point
drive.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
drive.execute_script("window.navigator.chrome = {runtime: {},  };")
drive.execute_script("window.navigator.permissions = {query: () => Promise.resolve({state: 'granted'}),  };")
drive.execute_script("const originalQuery = window.navigator.permissions.query; return window.navigator.permissions.query = (parameters) => (parameters.name === 'notifications' ? Promise.resolve({state: Notification.permission}) : originalQuery(parameters));")
drive.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5],  });")
drive.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});")


# fill the form
drive.find_element(By.NAME, 'name').send_keys(Faker().name())
drive.find_element(By.NAME, 'phone').send_keys('1'*10)

drive.implicitly_wait(10)
drive.find_element(By.ID, 'create_claim_form').submit()

input('Press ENTER to exit the program')