from selenium import webdriver
# we need chromedriver, so first download it
driver = webdriver.Chrome(executable_path="")#path of chromedriver.exe
driver.maximize_window()
driver.implicitly_wait(10)#can change the counter time


driver.get("https:www.google.com")
driver.find_element_by_name('q').send_keys('Hello world')# searches for hello world
driver.find_element_by_name('btnK').submit()
#driver.close()
