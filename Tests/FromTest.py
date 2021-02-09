import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/find_xpath_form')

driver.find_element_by_xpath("//input[@name='first_name']").send_keys("Maksym")
driver.find_element_by_xpath("//input[@name='last_name']").send_keys("Ovsiuk")
driver.find_element_by_xpath("//input[contains(@class,'city')]").send_keys("LVOV")
driver.find_element_by_xpath("//input[@id=\"country\"]").send_keys("UKRAINE")

driver.find_element_by_xpath("//*[text()='Submit']").click()

time.sleep(10)

driver.quit()
