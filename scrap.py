#Librerias
import pandas as pd
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def cookies_booking(url):
    PATH = ChromeDriverManager().install()    # Instala driver para usar Chrome

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-extensions")  # Disable extensions

    # Set up Chrome WebDriver with the configured options
    driver = webdriver.Chrome(PATH, options=chrome_options)

    driver.get(url)

    try:
        time.sleep(10)
        popup_button = driver.find_element(By.CLASS_NAME, 'fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.ae1678b153')
        actions = ActionChains(driver)
        actions.move_to_element(popup_button).click().perform()

        # Recursive call to handle any subsequent pop-up windows
        handle_popup_windows(driver)
    except:
        # No pop-up window found, continue with your scraping logic
        pass

    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]').click()  #Rechaza cookies

    return driver

# Function to handle pop-up windows
def handle_popup_windows(driver):
    try:
        time.sleep(10)
        popup_button = driver.find_element(By.CLASS_NAME, 'fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.ae1678b153')
        actions = ActionChains(driver)
        actions.move_to_element(popup_button).click().perform()

        # Recursive call to handle any subsequent pop-up windows
        handle_popup_windows(driver)
    except:
        # No pop-up window found, continue with your scraping logic
        pass

    try:
        time.sleep(10)
        popup_button = driver.find_element(By.XPATH, '//*[@id="b2theme_landing_indexPage"]/div[13]/div/button')
        actions = ActionChains(driver)
        actions.move_to_element(popup_button).click().perform()

        # Recursive call to handle any subsequent pop-up windows
        handle_popup_windows(driver)
    except:
        # No pop-up window found, continue with your scraping logic
        pass


def buscador_booking(driver, locator_checkin, locator_checkout, text=None):
    driver.get(driver.current_url)

    #handle_popup_windows(driver)

    #time.sleep(10)

   # driver.find_element(By.XPATH, '//*[@id="footer_links"]/div[1]/ul/li[6]/a').click()  #Filtra por Hoteles

    #time.sleep(5)
    handle_popup_windows(driver)

    #search_bar=driver.find_element(By.XPATH, '//*[@id="ss"]')
    search_bar=driver.find_element(By.XPATH, '//*[@id=":Ra9:"]')
    search_bar.click()  #Clicka en buscador

    #time.sleep(3)
    handle_popup_windows(driver)

    search_bar.send_keys(text)

    #time.sleep(3)
    handle_popup_windows(driver)

    driver.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[2]/div/div[1]/button[1]').click() #Clicka para abrir calendario

    #time.sleep(15)
    handle_popup_windows(driver)

    driver.find_element(By.XPATH, locator_checkin).click()  #Clicka en fecha checkin

    #time.sleep(15)
    handle_popup_windows(driver)

    driver.find_element(By.XPATH, locator_checkout).click()  #Clicka en fecha checkout

    #time.sleep(3)
    handle_popup_windows(driver)

    driver.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[4]/button').click()  #Clicka en boton 'BUSCAR'
    #driver.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]/button').click()  #Clicka en boton 'BUSCAR'

    handle_popup_windows(driver)

    time.sleep(10)

    driver.find_element(By.XPATH, "//div[contains(text(), 'Hoteles')]").click()#Clicka en filtro Hotel

    return driver

def scrap_booking(driver):
    results = []
    time.sleep(10)
    while True:
        handle_popup_windows(driver)
        tabla = driver.find_elements(By.CLASS_NAME, 'd20f4628d0')
        filas = [e.text.split('\n') for e in tabla]
        results.extend(filas)

        try:
            next_page_element = driver.find_element(By.XPATH, '//*[@id="search_results_table"]/div[2]/div/div/div[4]/div[2]/nav/div/div[3]/button')
            if next_page_element.is_enabled():
                next_page_element.click()
                time.sleep(10)
            else:
                break
        except NoSuchElementException:
            break

    return results
