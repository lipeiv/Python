from selenium import webdriver 
browser = webdriver.Chrome()

print(browser.find_elements_by_id("percent1"))
browser.close()