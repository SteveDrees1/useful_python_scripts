import os
import time

from selenium import webdriver
#
# os.chdir(r'C:\Users\BDDrees\Downloads\chromedriver_win32')
driver = webdriver.Chrome()  # Optional argument, if not specified,
# will search a path.

driver.get('https://www.google.com/');

time.sleep(5)  # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()