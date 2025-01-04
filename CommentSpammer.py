from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("Enter video link here")
time.sleep(5)


##Signing in
driver.find_element(by=By.LINK_TEXT, value="Sign in").click()
time.sleep(2)
driver.find_element(by=By.ID, value="identifierId").send_keys('Enter Gmail username here')
time.sleep(0)
next = driver.find_element(by=By.ID, value="identifierNext")
next.click()
time.sleep(2)
driver.find_element(by=By.NAME, value="Passwd").send_keys('Enter Gmail password here')
time.sleep(0)
next = driver.find_element(by=By.ID, value="passwordNext")
next.click()
time.sleep(10)

driver.execute_script("window.scrollTo(0, 2500)")
time.sleep(4)
driver.execute_script("window.scrollTo(0, 5)")
driver.execute_script("window.scrollTo(0, 2600)")
time.sleep(4)


##Adding comment
i = 0
comment_count = 1
while i < comment_count:


    text_box = driver.find_element(By.ID, "placeholder-area")
    text_box.click()
    time.sleep(0.5)
    comment_box = driver.find_element(By.ID, "contenteditable-root")
    keyword = "Enter some comment here"
    comment_box.send_keys(keyword)
    time.sleep(0.5)

    comment = driver.find_element(by=By.ID, value="submit-button")
    comment.click()
    time.sleep(2)

