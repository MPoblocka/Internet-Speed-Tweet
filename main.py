#STARTED with importing necessary packages
import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PROMISED_DOWN = 150
PROMISED_UP = 150
CHROME_DRIVER_PATH = "YOUR_DRIVER_PATH"
TWITTER_EMAIL = "YOUR_EMAIL"
TWITTER_PASSWORD = "YOUR_PASSWORD"
TWITTER_USERNAME = "YOUR_USERNAME"

#MADE A CLASS TO HAVE A CLEANER CODE
class InternetSpeedTwitterBot():

#CREATED CLASS VARIABLES
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.down= 0
        self.up= 0

#CREATED A METHOD WITHIN THE CLASS WHICH USES WEB SCRAPING TO SEARCH FOR MY INTERNET SPEED
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(5)

        self.accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        self.accept_button.click()
        time.sleep(5)

        self.go_button = self.driver.find_element(By.CLASS_NAME,"start-text")
        self.go_button.click()
        time.sleep(50)

        self.accept_cross = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a")
        self.accept_cross.click()
        time.sleep(5)

        self.nearly_down = self.driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        #print(self.nearly_down.text)
        self.down= self.nearly_down.text

        self.nearly_up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        #print(self.nearly_up.text)
        self.up = self.nearly_up.text
        self.driver.close()


#MADE ANOTHER CLASS WHICH SIGN TO MY TWITTER ACCOUNT AND PLACE A TWEET
    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/")
        time.sleep(5)
        self.cookies_button = self.driver.find_element(By.XPATH,
                                                       "//*[@id='layers']/div/div/div/div/div/div[2]/div[1]/div/span/span")
        self.cookies_button.click()
        time.sleep(5)
#SOMETIMES TWITTER WEBSITE OPENS AS A DIFFERENT VERSION AND THEN IT IS IMPOSIBLE TO LOCATE ELEMENTS.
#THAT IS WHY I USED TRY/EXCEPT METHOD TO LOAD THE PAGE AGAIN IF THAT HAPPENS
        try:
            self.sign_in_butt = self.driver.find_element(By.XPATH,
                                                         "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")

        except NoSuchElementException:
            self.driver.close()
            time.sleep(5)

            self.driver.get("https://twitter.com/")
            self.sign_in_butt = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
            self.sign_in_butt.click()
            time.sleep(5)

        else:
            self.sign_in_butt.click()
            time.sleep(5)

        finally:
            self.email_input = self.driver.find_element(By.TAG_NAME,"input")
            self.email_input.send_keys(TWITTER_EMAIL)
            self.email_input.send_keys(Keys.ENTER)
            time.sleep(5)

            self.username_input = self.driver.find_element(By.TAG_NAME, "input")
            self.username_input.send_keys(TWITTER_USERNAME)
            self.username_input.send_keys(Keys.ENTER)
            time.sleep(5)

            self.password_input = self.driver.find_element(By.NAME, "password")
            self.password_input.send_keys(TWITTER_PASSWORD)
            self.password_input.send_keys(Keys.ENTER)
            time.sleep(5)

            #self.twitter_post = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
            self.twitter_post = self.driver.find_element(By.CLASS_NAME,"public-DraftStyleDefault-block")
            self.twitter_post.send_keys(f"Hello, World! My internet speed is awesome today! {object_1.down}/{object_1.up}")

            self.tweet = self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
            self.tweet.click()
            time.sleep(5)

# CREATED OBJECT FROM THE CLASS
object_1 = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
#CALLED THE CLASS METHODS
object_1.get_internet_speed()
object_1.tweet_at_provider()






