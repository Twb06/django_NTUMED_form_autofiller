from selenium.webdriver.chrome import service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

import re
import time
import os

def autofiller(url):
    try:
        GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        #options.add_argument("--headless")

        chrome_options.binary_location = GOOGLE_CHROME_PATH
        
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        """webDriverServer = service.Service('./operadriver_win64/operadriver.exe')
        webDriverServer.start()

        capabilities = {
            'operaOptions': {
                'binary': 'C:/Program Files (x86)/Opera/launcher.exe'
            }
        }

        browser = webdriver.Remote(webDriverServer.service_url, webdriver.DesiredCapabilities.OPERA)"""
        #browser.maximize_window()

        browser.get(url)
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, 'html5lib')

        button_xpath = "//input[@value='Male' and @type='radio']"

        button_select_list = browser.find_elements_by_xpath(button_xpath)
        for button_select in button_select_list:
            if not button_select.is_selected():
                button_select.click()

        html_source = browser.page_source

        time.sleep(5)

        return html_source

    except Exception as e:
        raise e
        pass
    