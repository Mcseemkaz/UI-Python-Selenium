import time
import string
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/huge_form.html')

fields = driver.find_elements(By.XPATH, '//input[@type=\'text\']')


def get_random_string(num_chars):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(num_chars))
    return result_str


for element in fields:
    element.send_keys(get_random_string(10))

driver.find_element_by_xpath('//button[@type=\'submit\']').click()

time.sleep(10)
