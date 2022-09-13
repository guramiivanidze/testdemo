from selenium.webdriver.common.by import By

import data.textboxdata as data
from Configuration import config


driver = config.DRIVER
driver.get(config.BASE_URL +"text-box")

elements= {
    "full_name_input":(By.ID, "userName"),
    "userEmail_input":(By.ID, "userEmail"),
    "current_Address_input":(By.ID, "userName"),
    "permanent_Address_input":(By.ID, "userName"),
    "submit":(By.ID, "submit"),
}



driver.find_element(*elements["full_name_input"]).send_keys(data.names["first_name"])

def test_enter_all_data():
    driver.find_element(*elements["full_name_input"]).send_keys(data.names["first_name"])
    driver.find_element(*elements["full_name_input"]).send_keys(data.names["first_name"])
    driver.find_element(*elements["full_name_input"]).send_keys(data.names["first_name"])
    driver.find_element(*elements["full_name_input"]).send_keys(data.names["first_name"])