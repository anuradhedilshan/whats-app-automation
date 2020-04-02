# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait


# driver  = webdriver.Chrome("F:\Seleuium web driver for Chrome 80\chromedriver.exe")
# driver.maximize_window()  
# driver.get("https://web.whatsapp.com")
# wait = WebDriverWait(driver, 600) 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
contact = "Kavindu"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Chrome("F:\Seleuium web driver for Chrome 80\chromedriver.exe")
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

el =  driver.find_element_by_css_selector('span[title="PERFUME FANZ❣ॐ"]')

time.sleep(2)
print("element geted or ",el)
el.click()
print("element selected")


text =  'Hacking All Accounts '

input = driver.find_element_by_css_selector("div[data-tab='1']")

for i in range(1000):
    input.send_keys(1+i)
    input.send_keys(Keys.ENTER)


input.send_keys("Face book Post walata mehema comment karanu lebe 1comment =  100rs" + Keys.ENTER)
print("Message sent")



