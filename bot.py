from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller # pip install chromedriver-autoinstaller
import time

chromedriver_autoinstaller.install() # To update your chromedriver automatically
driver = webdriver.Chrome()

# Get free proxies for rotating
def get_free_proxies(driver):
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)
    
    return proxies


free_proxies = get_free_proxies(driver)

print('free_proxies:' + free_proxies[0]['IP Address']+':'+free_proxies[0]['Port'])

options = Options()
options.add_experimental_option=True

webBrowser = webdriver.Chrome(options=options)
url = 'https://www.youtube.com/watch?v=Rn-XbNq6VAs&ab_channel=Canalemdia'

def open_new_tab(url, tab_number):
    webBrowser.execute_script("window.open('about:blank', "+ str(tab_number) +");")
    webBrowser.switch_to.window(str(tab_number) )
    webBrowser.get(url)

while True:
    for i in range(10):
        options.add_argument('--proxy-server=http://%s' % free_proxies[i]['IP Address']+':'+free_proxies[i]['Port'])
        open_new_tab(url, i)
        time.sleep(5)
        if i == 0:
            video = webBrowser.find_element(By.ID, 'movie_player')
            video.send_keys(Keys.SPACE) #hits space
        time.sleep(5)

    time.sleep(105)