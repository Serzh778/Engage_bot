import automatation.constant as const
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class automate(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False): 
        self.driver_path = driver_path 
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super().__init__()  # Call the __init__ method of the parent class explicitly
        self.implicitly_wait(15)
        self.maximize_window()
    
    def land_on_the_page(self):
        self.get(const.BASE_URL)  #lands on the first page
    
    def input_username(self,username): #for imputing username
        user = self.find_element(By.ID, 'ctl00_PageContent_loginControl_txtUN')
        user.click()
        user.send_keys(username) #input
    
    def input_password(self,password): # for inputing password
        password1 = self.find_element(By.ID, 'ctl00_PageContent_loginControl_txtPwd')
        password1.click()
        password1.send_keys(password) #input
    
    def submit(self): # submiting username and password
        submit_button = self.find_element(By.ID, 'ctl00_PageContent_loginControl_btnLogin')
        submit_button.click()

    def timetable(self): # clicks the timetable icon to show the timetable
        timetable_button = self.find_element(By.XPATH, "//li[@class='greyPane']/a[@href='/VLE/WeeklyTimetable.aspx']")
        timetable_button.click()
    def next_week_arrow(self): # clicks the next week arrow
        try:
            for i in range(2):
                arrow = self.find_element(By.ID, 'ctl00_PageContent_weeklyTimetable_wsTimetableDate_btnNextWeek')
                arrow.click()
                time.sleep(2)


        except StaleElementReferenceException:
           
            for i in range(2): 
                arrow = self.find_element(By.ID, 'ctl00_PageContent_weeklyTimetable_wsTimetableDate_btnNextWeek')
                arrow.click()

