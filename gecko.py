from selenium import webdriver
browser = webdriver.Chrome()

browser.get("http://www.lipeipei.com.cn")
print(browser.page_source)
browser.close()