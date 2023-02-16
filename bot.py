from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

#url = 'https://www.youtube.com/watch?v=k2eEyOZmi2c&ab_channel=CanalemDia'
options = Options()
options.add_experimental_option=True

webBrowser = webdriver.Chrome(options=options)
url = 'https://www.youtube.com/watch?v=k2eEyOZmi2c&ab_channel=CanalemDia'

def open_new_tab(url, tab_number):
    webBrowser.execute_script("window.open('about:blank', "+ str(tab_number) +");")
    webBrowser.switch_to.window(str(tab_number) )
    webBrowser.get(url)

while True:
    for i in range(10):
        open_new_tab(url, i)

    time.sleep(90)


