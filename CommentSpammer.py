from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=YZtzNN6YDwk&ab_channel=vauvau")
time.sleep(5)


##Signing in
driver.find_element(by=By.LINK_TEXT, value="Sign in").click()
time.sleep(2)
driver.find_element(by=By.ID, value="identifierId").send_keys('commentspammer101@gmail.com')
time.sleep(0)
next = driver.find_element(by=By.ID, value="identifierNext")
next.click()
time.sleep(2)
driver.find_element(by=By.NAME, value="Passwd").send_keys('noobcomments')
time.sleep(0)
next = driver.find_element(by=By.ID, value="passwordNext")
next.click()
time.sleep(15)

##Adding comment
text_box = driver.find_element(By.ID, "contenteditable-root")
text_box.click()
keyword = "Best video ever"
text_box.send_keys(keyword)
time.sleep(5)

comment = driver.find_element(by=By.XPATH, value="submit-button")
comment.click()

"""

time.sleep(10)

email = "commentspammer101@gmail.com"
password = "noobcomments"
video_url = "https://www.youtube.com/watch?v=YZtzNN6YDwk&ab_channel=vauvau" 
comment_text = "Best video ever"  

"""

