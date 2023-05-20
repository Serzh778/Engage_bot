import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from automatation.processes import automate

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

with automate() as bot:
    bot.land_on_the_page()
    time.sleep(1)
    bot.input_username('24rserzh@regents.ac.th')
    time.sleep(1)
    bot.input_password('serzh778')
    time.sleep(1)
    bot.submit()
    time.sleep(1)
    bot.timetable()
    time.sleep(2)
    bot.next_week_arrow()
    time.sleep(3)
    bot.timetable_row(1)
    time.sleep(1000)
