from selenium.webdriver.common.by import By

import data.textboxdata as data
from Configuration import config
import unittest


class TestTextboxpage(unittest.TestCase):
    elements = {
        "full_name_input": (By.ID, "userName"),
        "userEmail_input": (By.ID, "userEmail"),
        "current_Address_input": (By.ID, "currentAddress"),
        "permanent_Address_input": (By.ID, "permanentAddress"),
        "submit": (By.ID, "submit"),
    }

    # self.driver.find_element(*self.elements["full_name_input"]).send_keys(data.names["first_name"])
    def setUp(self):
        self.driver = config.DRIVER
        self.driver.get(config.BASE_URL + "text-box")

    def test_Is_name_Show(self):
        self.driver.find_element(*self.elements["full_name_input"]).send_keys(data.names["first_name"])
        self.driver.find_element(*self.elements["userEmail_input"]).send_keys(data.emails["random_email"])
        self.driver.find_element(*self.elements["current_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["permanent_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["submit"]).click()

        self.assertEqual(self.driver.find_element(By.ID, "name").text,
                         "Name:" + data.names["first_name"],
                         )

    def test_Is_email_show(self):
        self.driver.find_element(*self.elements["full_name_input"]).send_keys(data.names["first_name"])
        self.driver.find_element(*self.elements["userEmail_input"]).send_keys(data.emails["random_email"])
        self.driver.find_element(*self.elements["current_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["permanent_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["submit"]).click()

        self.assertEqual(self.driver.find_element(By.ID, "email").text,
                         "Email:" + data.emails["random_email"],
                         )

    def test_Is_CurrentAddress_show(self):
        self.driver.find_element(*self.elements["full_name_input"]).send_keys(data.names["first_name"])
        self.driver.find_element(*self.elements["userEmail_input"]).send_keys(data.emails["random_email"])
        self.driver.find_element(*self.elements["current_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["permanent_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["submit"]).click()

        self.assertEqual(self.driver.find_element(By.ID, "currentAddress").text,
                         "Current Address :" + data.current_Address["full_address"],
                         )

    def test_Is_permanentAddress_show(self):
        self.driver.find_element(*self.elements["full_name_input"]).send_keys(data.names["first_name"])
        self.driver.find_element(*self.elements["userEmail_input"]).send_keys(data.emails["random_email"])
        self.driver.find_element(*self.elements["current_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["permanent_Address_input"]).send_keys(
            data.current_Address["full_address"])
        self.driver.find_element(*self.elements["submit"]).click()

        self.assertEqual(self.driver.find_element(By.ID, "permanentAddress").text,
                         "Permanent Address :" + data.current_Address["full_address"],
                         )

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)