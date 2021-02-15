import time
import unittest
from selenium import webdriver


class TestRegistrationForm(unittest.TestCase):
    def test_registration_form_one(self):
        driver = webdriver.Chrome()

        driver.get('http://suninjuly.github.io/registration1.html')

        driver.find_element_by_xpath("//label[text()='First name*']/following-sibling::input").send_keys("Maksym")
        driver.find_element_by_xpath("//label[text()='Last name*']/following-sibling::input").send_keys("Ovsiuk")
        driver.find_element_by_xpath("//label[text()='Email*']/following-sibling::input").send_keys("LVOV")

        driver.find_element_by_xpath("//*[text()='Submit']").click()

        time.sleep(5)

        driver.quit()

    def test_registration_form_two(self):
        driver = webdriver.Chrome()

        driver.get('http://suninjuly.github.io/registration2.html')

        driver.find_element_by_xpath("//label[text()='First name*']/following-sibling::input").send_keys("Maksym")
        driver.find_element_by_xpath("//label[text()='Last name*']/following-sibling::input").send_keys("Ovsiuk")
        driver.find_element_by_xpath("//label[text()='Email*']/following-sibling::input").send_keys("LVOV")

        driver.find_element_by_xpath("//*[text()='Submit']").click()

        time.sleep(5)

        driver.quit()

    if __name__ == "__main__":
        unittest.main()
