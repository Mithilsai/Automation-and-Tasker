import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedinBot:
    def __init__(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """
        # we need chromedriver, so first download it

        self.driver = webdriver.Chrome(executable_path="")#path of chromedriver.exe

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)#can change the counter time

        self.username = username
        self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self, username, password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()
        #self.driver.execute_script("window.scrollBy(0,500)","")
        #the above one is used to go to that pixel(0,500)->0 is the starting, 500 is the ending



if __name__ == '__main__':

    username = ''# Enter your username credential
    password = ''# Enter your password credential

    bot = LinkedinBot(username, password)
    bot.login(username, password)
