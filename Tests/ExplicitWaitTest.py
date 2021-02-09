import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def func(value):
    return str(math.log(abs(12 * math.sin(value))))


driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

driver.find_element_by_id("book").click()

x_value = float(driver.find_element_by_id("input_value").text)

print(x_value)

driver.find_element_by_id("answer").send_keys(func(x_value))
driver.find_element_by_xpath("//*[text()='Submit']").click()

time.sleep(5)

driver.quit()
