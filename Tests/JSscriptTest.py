import math
import time
from selenium import webdriver


def func(value):
    return math.log(abs(12 * math.sin(value)))


driver = webdriver.Chrome()
driver.get('http://SunInJuly.github.io/execute_script.html')

x = float(driver.find_element_by_id("input_value").text)

driver.find_element_by_id("answer").send_keys(str(func(x)))
submit_button = driver.find_element_by_tag_name("button")

driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
driver.find_element_by_id("robotCheckbox").click()
driver.find_element_by_id("robotsRule").click()
submit_button.click()

time.sleep(5)

driver.quit()
