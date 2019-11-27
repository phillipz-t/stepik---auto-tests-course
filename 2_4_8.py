from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pyperclip
import math



def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'),'$100'))
browser.find_element(By.ID, 'book').click()

browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, 'input_value').text))
browser.find_element(By.ID, 'solve').click()

alert = browser.switch_to.alert
alert = alert.text
alert = alert.split(': ')[-1]
pyperclip.copy(alert)


