import random
import string
import time

from selenium import webdriver


def get_random_string(num_chars):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(num_chars))
    return result_str


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/registration2.html')


elements = driver.find_elements_by_xpath("//input[@required]")

print(len(elements))
assert len(elements) == 3

for element in elements:
    element.send_keys(get_random_string(5))

driver.find_element_by_xpath("//*[text()='Submit']").click()

time.sleep(3)

assert "Congratulations! You have successfully registered!" == driver.find_element_by_tag_name("h1").text
driver.quit()
