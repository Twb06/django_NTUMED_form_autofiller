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

# Celery-progress
from celery_progress.backend import ProgressRecorder


def buttonSelectionClick(button_xpath, browser):   
    # fill in evaluation form
    # select "A_perfect"(button_xpath = "//input[@value='2']") for all radio buttons
    button_select_list = browser.find_elements_by_xpath(button_xpath)
    scroll_into_view_status = False
    for button_select in button_select_list:
        if not button_select.is_selected():
            # scroll the element into view to interact, 
            # and constrain it to run only once to save time
            if not scroll_into_view_status:
                browser.execute_script("arguments[0].scrollIntoView();", button_select)
                scroll_into_view_status = True
            button_select.click()
    
    return

def nextPage(browser):
    # next page
    next_page_button = browser.find_element_by_xpath("//button[@name='submit-btn-saverecord']")
    browser.execute_script("arguments[0].scrollIntoView();", next_page_button)
    next_page_button.click()
    time.sleep(0.1)
    
    return
    
def previousPage(browser):
    # previous page
    previous_page_button = browser.find_element_by_xpath("//button[@name='submit-btn-saveprevpage']")
    browser.execute_script("arguments[0].scrollIntoView();", previous_page_button)
    previous_page_button.click()
    time.sleep(0.1)
    
    return

"""def manualFillin(courses_name_list, n_course):
    while True:
        try:
            manual_fillin_confirm_input = input("Manually fillin?(y/n)").lower()
        # rule out unexpected input, and restart the process
        except:
            print("Error! Please enter again!")
            time.sleep(1.5)
            os.system("cls")

        # user confirm
        if manual_fillin_confirm_input == "y":
            break
        elif manual_fillin_confirm_input == "n":
            time.sleep(1.5)
            os.system("cls")
            
            return
        # rule out unexpected input, and restart the process
        else:
            print("Undefined character! Please enter again!")
            time.sleep(1.5)
            os.system("cls")
            continue
    
    for course_name in courses_name_list:
        print(course_name)
    manual_fillin_page_list = input("\n\nWhich course do you want to fill in on your own? eg. type\"1 2 4 6\"\n").split()
    # turn to target page
    for manual_fillin_page in manual_fillin_page_list:
        target_page = int(manual_fillin_page)

        while True:
            # reload current page html source
            html_source = browser.page_source
            soup = BeautifulSoup(html_source, 'html5lib')
            current_page = int( soup.find(id = "surveypagenum").string.split()[1] )
            if current_page == target_page:
                input("If you finished the page, press any button to continue...")
                if manual_fillin_page == manual_fillin_page_list[-1]:
                    if target_page != n_course:
                        target_page = n_course
                        continue
                    else:
                        break
                else:
                    break
            elif current_page > target_page:
                previousPage()
                continue
            elif current_page < target_page:
                nextPage()
                continue
"""
def autofiller(task, url, teacher_index_input):
    try:
        GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        
        chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)

        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        #options.add_argument("--headless")

        chrome_options.binary_location = chrome_bin
        
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

        print("start browser complete!@autofiller.py")

        # open form
        browser.get(url)
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, 'html5lib')
        time.sleep(1)

        print("test celery progress complete!@autofiller.py")

        # select teacher
        teacher_button_xpath = "//td[@class='data col-5']//input[@value=" + teacher_index_input + "]"
        # get total course num
        n_course = int( soup.find(id = "surveypagenum").string.split()[-1] )
        # list for storing courses' name
        courses_name_list = []

        # grades for evaluation button xpath
        #     "N/A"(button_xpath = "//input[@value='1']")
        #     "A_perfect"(button_xpath = "//input[@value='2']")
        #     "B_good"(button_xpath = "//input[@value='3']")
        #     "C_normal"(button_xpath = "//input[@value='4']")
        evaluation_button_xpath = "//td[@class='data choicematrix']//input[@value='2' and @type='radio']"

        # Create the progress recorder instance
	    # which we'll use to update the web page
        progress_recorder = ProgressRecorder(self)

        # fill in form
        # loop pages of courses while recording names of all courses, 
        # which can be manually fill in in the end of the process
        for course_index in range(1, n_course + 1):
            # reload current page html source
            html_source = browser.page_source
            soup = BeautifulSoup(html_source, 'html5lib')
            current_page = int( soup.find(id = "surveypagenum").string.split()[1] )
            
            # Update progress on the web page
            progress_recorder.set_progress(course_index, n_course, description="Processing")

            # prevent error from form which was not completed
            if course_index < current_page:
                continue
            
            # record names of all courses
            course_name = soup.find("td", class_ = "header toolbar").find_all(text = True)[0]
            courses_name_list.append( course_name )
            
            # auto fillin
            buttonSelectionClick(evaluation_button_xpath, browser)
            # exclude bedside learning courses
            if "分組老師" or "實習老師" in course_name:
                buttonSelectionClick(teacher_button_xpath, browser)
            
            # next page, preventing sent out in the end
            if course_index == n_course:
                break
            else:
                nextPage(browser)

        # save and let user check result and manually sent form (open in alpha_v_*.0)
        save_button = browser.find_element_by_xpath("//button[@name= 'submit-btn-savereturnlater']")
        save_button.click()
        
        # manually fillin (not open in alpha_v_1.0)
        """manualFillin(courses_name_list, n_course)"""

        # sent (open in alpha_v_*.1)
        """nextPage()

        finish_button = browser.find_element_by_xpath("//button[@class = 'jqbuttonmed ui-button ui-corner-all ui-widget']")
        finish_button.click()"""
        
        # setting return list for HttpRespond in views.py
        """http_respond_list = ["<p>Success filling:</p><ol>"]
        for courses_name in courses_name_list:
            http_respond_list.append("<li>" + courses_name + "</li>")
        http_respond_list.append("</ol>")
        http_respond_list.append("<p>----Alpha v 1.0----</p>")
        http_respond_list.append("<a href=" + url + ">Please manually check and send your form!</a>")

        return http_respond_list"""

        # close all opened browser window and terminates the WebDriver session
        driver.quit()

    except Exception as e:
        raise e
        pass
    