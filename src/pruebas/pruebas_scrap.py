#Librerias
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import numpy as np


PATH = ChromeDriverManager().install()    # instala driver de chrome

driver = webdriver.Chrome(PATH)      # abre una ventana de chrome

#Busqueda didn´t work, I had to type up the whole URL + search

URL='https://www.booking.com'

driver.get(URL)

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]').click()  #Rechaza cookies

time.sleep(5)

search_bar=driver.find_element(By.XPATH, '//*[@id=":Ra9:"]')
search_bar.click()  #Clicka en buscador

time.sleep(3)

text='Madrid, Chamartin' #Originalmente NONE
search_bar.send_keys(text)

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[2]/div/div/button[1]').click() #Clicka para abrir calendario

time.sleep(10)

locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[5]/span'
driver.find_element(By.XPATH, locator_checkin).click()  #Clicka en fecha checkin

time.sleep(10)

locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[6]/span'
driver.find_element(By.XPATH, locator_checkout).click()  #Clicka en fecha checkout

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[4]/button').click()  #Clicka en boton 'BUSCAR'

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="filter_group_popular_:Rkq:"]/div[4]/label').click()  #Filtra por Hoteles

time.sleep(3)

tabla = driver.find_elements(By.CLASS_NAME, 'd20f4628d0')

filas = [e.text.split('\n') for e in tabla]

pd.DataFrame(filas)
