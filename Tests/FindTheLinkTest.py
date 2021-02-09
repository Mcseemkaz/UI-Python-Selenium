import math
import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/find_link_text')

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

print("Link text is {}".format(link_text))

driver.find_element_by_link_text(link_text).click()

time.sleep(1)

driver.find_element_by_xpath("//input[@name='first_name']").send_keys("Maksym")
driver.find_element_by_xpath("//input[@name='last_name']").send_keys("Ovsiuk")
driver.find_element_by_xpath("//input[contains(@class,'city')]").send_keys("LVOV")
driver.find_element_by_xpath("//input[@id=\"country\"]").send_keys("UKRAINE")

time.sleep(1)

submit_button = driver.find_element_by_xpath("//button[text()='Submit']")

print(submit_button)

submit_button.click()

time.sleep(10)

driver.quit()