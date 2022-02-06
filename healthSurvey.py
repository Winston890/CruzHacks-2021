from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#Download webdriver for your version of chrome here https://chromedriver.chromium.org/downloads
#Note: Must have Webdriver added to PATH after downloading binary
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

#CruzID = input("Enter CruzID: ")
#GoldPassword = input ("Enter Gold Password: ")

driver.get("https://studenthealth.ucsc.edu/confirm.aspx")

#Can't be showing my cruz id and password online
login_CruzID = driver.find_element_by_id("username").send_keys("cruzID")
login_password = driver.find_element_by_id("password").send_keys("Gold Password")
element = driver.find_element_by_name("_eventId_proceed")
element.click()

remember_me = driver.find_element_by_xpath("//*[@id=\"login-form\"]/div[2]/div/label/input").click()
duo_auth = driver.find_element_by_partial_link_text("Send").click()
