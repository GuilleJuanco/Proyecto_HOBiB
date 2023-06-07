from scrap import cookies_booking, buscador_booking, scrap_booking
from clean import clean_csv
import pandas as pd
import numpy as np

#Scrapeo.
"""
#Variables
url='https://www.booking.com/'
text='Comunidad de Madrid'

#Segundo finde 1 dia.
locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[5]'
locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[6]'
#locator_checkin='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[5]'
#locator_checkout='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[6]'

# Perform cookie handling
driver = cookies_booking(url)

# Perform search
driver = buscador_booking(driver, locator_checkin, locator_checkout, text=text)

# Perform scraping
search_results1 = scrap_booking(driver)

#Store data
second_oneday = pd.DataFrame(search_results1)

#Export to csv
second_oneday.to_csv('21.csv', index=False)


# Close the driver
driver.quit()

#Segundo finde 2 dias.
locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[5]'
locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[7]'
#locator_checkin='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[5]'
#locator_checkout='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[7]'

# Perform cookie handling
driver = cookies_booking(url)

# Perform search
driver = buscador_booking(driver, locator_checkin, locator_checkout, text=text)

# Perform scraping
search_results2 = scrap_booking(driver)

#Store data
second_twodays = pd.DataFrame(search_results2)

#Export to csv
second_twodays.to_csv('22.csv', index=False)

#Tercer finde 1 dia.
locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[3]/td[5]'
locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[3]/td[6]'
#locator_checkin='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[5]'
#locator_checkout='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[6]'

# Perform cookie handling
driver = cookies_booking(url)

# Perform search
driver = buscador_booking(driver, locator_checkin, locator_checkout, text=text)

# Perform scraping
search_results3 = scrap_booking(driver)

#Store data
third_oneday = pd.DataFrame(search_results3)

#Export to csv
third_oneday.to_csv('31.csv', index=False)

# Close the driver
driver.quit()

#Tercer finde 2 dias.
locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[3]/td[5]'
locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[3]/td[7]'
#locator_checkin='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[5]'
#locator_checkout='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[3]/td[7]'

# Perform cookie handling
driver = cookies_booking(url)

# Perform search
driver = buscador_booking(driver, locator_checkin, locator_checkout, text=text)

# Perform scraping
search_results4 = scrap_booking(driver)

#Store data
third_twodays = pd.DataFrame(search_results4)

#Export to csv
third_twodays.to_csv('32.csv', index=False)

# Close the driver
driver.quit()

#Cuarto finde 1 dia.
locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[4]/td[5]'
locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[4]/td[6]'
#locator_checkin='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[4]/td[5]'
#locator_checkout='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[4]/td[6]'

# Perform cookie handling
driver = cookies_booking(url)

# Perform search
driver = buscador_booking(driver, locator_checkin, locator_checkout, text=text)

# Perform scraping
search_results5 = scrap_booking(driver)

#Store data
fourth_oneday = pd.DataFrame(search_results5)

#Export to csv
fourth_oneday.to_csv('41.csv', index=False)

# Close the driver
driver.quit()

#Cuarto finde 2 dias.
locator_checkin='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[4]/td[5]'
locator_checkout='//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[4]/td[7]'
#locator_checkin='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[4]/td[5]'
#locator_checkout='//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[4]/td[7]'

# Perform cookie handling
driver = cookies_booking(url)

# Perform search
driver = buscador_booking(driver, locator_checkin, locator_checkout, text=text)

# Perform scraping
search_results6 = scrap_booking(driver)

#Store data
fourth_twodays = pd.DataFrame(search_results6)

#Export to csv
fourth_twodays.to_csv('42.csv', index=False)

# Close the driver
driver.quit()
"""
#Limpieza y transformación.

#Fechas y estancia + concatenar DFs

#Segundo finde 1 dia

df1 = clean_csv('src/data/21.csv')

#Crea columna con fecha checkin
df1['checkin'] = pd.to_datetime('2023-06-09')

#Crea columna con tipo de plan
df1['plan'] = '1 dia'

#Segundo finde 2 dias

df2 = clean_csv('src/data/22.csv')

#Crea columna con fecha checkin
df2['checkin'] = pd.to_datetime('2023-06-09')

#Crea columna con tipo de plan
df2['plan'] = '2 dias'

#Tercer finde 1 dia

df3 = clean_csv('src/data/31.csv')

#Crea columna con fecha checkin
df3['checkin'] = pd.to_datetime('2023-06-16')

#Crea columna con tipo de plan
df3['plan'] = '1 dia'

#Tercer finde 2 dias

df4 = clean_csv('src/data/32.csv')

#Crea columna con fecha checkin
df4['checkin'] = pd.to_datetime('2023-06-16')

#Crea columna con tipo de plan
df4['plan'] = '2 dias'

#Cuarto finde 1 dia

df5 = clean_csv('src/data/41.csv')

#Crea columna con fecha checkin
df5['checkin'] = pd.to_datetime('2023-06-23')

#Crea columna con tipo de plan
df5['plan'] = '1 dia'

#Cuarto finde 2 dias

df6 = clean_csv('src/data/42.csv')

#Crea columna con fecha checkin
df6['checkin'] = pd.to_datetime('2023-06-23')

#Crea columna con tipo de plan
df6['plan'] = '2 dias'

#Concatenar

booking = pd.concat([df1, df2, df3, df4, df5, df6], axis=0)

#Exportar

booking.to_csv('booking.csv', index=False)