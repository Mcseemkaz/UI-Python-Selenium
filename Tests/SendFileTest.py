import os
import string
import random
import time

from selenium import webdriver


def get_random_string(num_chars):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(num_chars))
    return result_str


driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/file_input.html')


fields = driver.find_elements_by_xpath("//input[@type='text']")

for field in fields:
    field.send_keys(get_random_string(5))

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)

driver.find_element_by_xpath("//input[@type='file']").send_keys(file_path)
driver.find_element_by_xpath("//button[@type='submit']").click()

print(current_dir)
print(file_path)

time.sleep(5)

driver.quit()


driver.quit()
