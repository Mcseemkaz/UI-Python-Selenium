import math
import time

from selenium import webdriver


def func(value):
    return str(math.log(abs(12 * math.sin(value))))


driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/redirect_accept.html')

driver.find_element_by_css_selector("button.trollface").click()

time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

x_value = float(driver.find_element_by_id("input_value").text)

print(x_value)

driver.find_element_by_id("answer").send_keys(func(x_value))
driver.find_element_by_xpath("//*[text()='Submit']").click()

time.sleep(5)

driver.quit()
