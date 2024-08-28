from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Constants
DRIVER_PATH = "C:/Development/chromedriver.exe"
TARGET_ACCOUNT = "gordongram"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

# For Driver Set Up
options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path=DRIVER_PATH)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        time.sleep(2)
        facebook = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button')
        facebook.click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

    def find_followers(self):
        push = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        push.click()
        time.sleep(2)
        search_btn = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div')
        search_btn.click()
        time.sleep(2)
        search_bar = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search_bar.send_keys(TARGET_ACCOUNT)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)
        target_account = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]')
        target_account.click()
        time.sleep(5)
        following = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        following.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


    def follow(self):
        

bot = InstaFollower()
bot.login()
bot.find_followers()
# bot.follow()