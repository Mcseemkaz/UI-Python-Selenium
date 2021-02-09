import math
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/selects2.html')

x_value = int(driver.find_element_by_id("num1").text)
y_value = int(driver.find_element_by_id("num2").text)


calc = x_value + y_value

select = Select(driver.find_element_by_id("dropdown"))

select.select_by_visible_text(str(calc))

driver.find_element_by_xpath("//*[text()='Submit']").click()

time.sleep(5)

driver.quit()
