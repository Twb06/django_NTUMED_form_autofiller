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
        webDriverServer = service.Service('./operadriver_win64/operadriver.exe')
        webDriverServer.start()

        capabilities = {
            'operaOptions': {
                'binary': 'C:/Program Files (x86)/Opera/launcher.exe'
            }
        }

        browser = webdriver.Remote(webDriverServer.service_url, webdriver.DesiredCapabilities.OPERA)
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
    