import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from automation.processes import automate

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

with automate() as bot:
    bot.land_on_the_page()  # Land on the web page
    time.sleep(1)  # Wait for 1 second
    bot.input_username('****')  # Input the username
    time.sleep(1)  # Wait for 1 second
    bot.input_password('****')  # Input the password
    time.sleep(1)  # Wait for 1 second
    bot.submit()  # Submit the username and password
    time.sleep(1)  # Wait for 1 second
    bot.timetable()  # Click the timetable icon
    time.sleep(2)  # Wait for 2 seconds
    bot.next_week_arrow()  # Click the next week arrow
    time.sleep(3)  # Wait for 3 seconds
    bot.timetable_row(1)  # Perform some action on the timetable row
    time.sleep(1000)  # Wait for a long duration
