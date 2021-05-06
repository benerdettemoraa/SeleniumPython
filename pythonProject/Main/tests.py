from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("LinkedIn Login")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.find_element_by_partial_link_text("LinkedIn Login").click()
driver.close()




