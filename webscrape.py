from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class webscrape: 
    def get_elements(url,type):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(url)
            elements = driver.find_elements(By.TAG_NAME, type) 
            texts = [element.text for element in elements]

            return texts

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

        finally:
            driver.quit()



#    texts = get_elements("https://brandeisjudges.com/sports/2023/7/24/gosman-sports-and-convocation-center.aspx","h3")
#    print("\nFound Elements:")
#    for i, text in enumerate(texts, 1):
#        print(f"{i}. {text}")
