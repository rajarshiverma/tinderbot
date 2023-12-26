from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from login_details import phone, password

class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)  # Create a WebDriverWait instance with a timeout of 10 seconds

    def open_driver(self):
        self.driver.get('https://tinder.com')
        self.accept_cookies()
        self.login()
        sleep(10)
        # self.right_swipe()
        self.autoswipe()
        # sleep(200)  # Sleep for 200 seconds (adjust as needed)

    def accept_cookies(self):
        cookies_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")))
        cookies_button.click()

    def login(self):
        #click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")))
        login_button.click()

        #facebook_login(self):
        time1 = [5,6,7,8,9,10,11]
        time2 = [10,11,12,13,14,15,16]
        # more_options_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button")))
        sleep(random.choice(time1))
        more_options_button = self.driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button")
        more_options_button.click()
        sleep(random.choice(time2)) 
        facebook_option = self.driver.find_element("xpath","/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]")                                                               
        # facebook_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]")))
        facebook_option.click()

        sleep(2)
        base_window =self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]

        #switch to FB window
        self.driver.switch_to.window(fb_popup_window)
        phone_box=self.driver.find_element("xpath","/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
        password_box=self.driver.find_element("xpath","/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
        login_box=self.driver.find_element("xpath","/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]")

        phone_box.send_keys(phone)
        password_box.send_keys(password)
        sleep(5)
        login_box.click()
        self.driver.switch_to.window(base_window)

        #after logging removing pop ups if present
        try:
            allow_location = self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")))
            allow_location.click()
        except:
            print("No location popup")
        
        try:
            notification = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]")))
            notification.click()
        except:
            print("No notification popup")
     
    def right_swipe(self):      
        like = self.driver.find_element("xpath","//*[@id='Tinder']/body")
        like.send_keys(Keys.ARROW_RIGHT)
        # sleep(1)
        # dislike = self.driver.find_element("xpath","//*[@id='Tinder']/body")
        # dislike.send_keys(Keys.ARROW_LEFT)
    
    def autoswipe(self):
        while True:
            sleep(2)
            try:
                self.right_swipe()
            except:
                try:
                    add_home = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]")))
                    add_home.click()
                except:
                    self.close_match()


    def close_match(self):
        match_popup = self.driver.find_element('xpath','//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    
    def get_matches(self):
        match_profiles = self.driver.find_element('class name','matchListItem')
        print(len(match_profiles))
        message_links = []
        for profile in match_profiles:
            if profile.get_attribute('href') == 'https//tinder.com/app/my-likes':
                continue
            message_links.append(profile.get_attribute('href'))
        return message_links

    def send_messages_to_matches(self):
        links=self.get_matches()
        for link in links:
            self.send_message(link)

    def send_message(self,link):
        self.driver.get(link)
        sleep(2)
        text_area = self.driver.find_element("xpath","/html/body/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea")

        text_area.send_keys('Hi !!')

        send_button = self.driver.find_element("xpath","/html/body/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button")
        try:
            send_button.click()
        except:
            send_button.send_keys(Keys.ENTER)

def main():
    bot = Tinderbot()
    bot.open_driver()
    bot.send_messages_to_matches()
if __name__ == "__main__":
    main()
