import math
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/get_attribute.html')

x_value = driver.find_element_by_id("treasure").get_attribute("valuex")

calc = str(math.log(abs(12 * math.sin(int(x_value)))))

driver.find_element_by_id("answer").send_keys(calc)
driver.find_element_by_id("robotCheckbox").click()
driver.find_element_by_id("robotsRule").click()

driver.find_element_by_xpath("//*[text()='Submit']").click()

time.sleep(5)

driver.quit()
