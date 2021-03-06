#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Aug 30, 2018

Course work: 

@author: Nirosha

Source:
      https://www.toptal.com/python/twitter-data-mining-using-python  
'''


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from io import BytesIO


def get_random_int(start, end):
    return random.randint(start, end)



def get_li_info_from_page(driver, li_dev_url, counter):
    '''
        get Linkedin info and save as png
    '''   
    driver.get(li_dev_url)
    
    
    wait = WebDriverWait(driver, 100)
    
    driver.execute_script("window.scrollTo(0, 1100)")
    
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pv-profile-section')))    
    driver.get_screenshot_as_file(str(counter) + '.png')
    
    
    
    
def login_and_create_base(li_links):

    # Google Chrome 
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    
    driver.get('https://linkedin.com')
    
        
    #type and find
    search = driver.find_element_by_name('session_key').send_keys('**********')    
    driver.find_element_by_name('session_password').send_keys('*****')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    
    counter = 0
    for link in li_links:
        counter += 1        
        print(link)
        
        # do try catch
        try:
            get_li_info_from_page(driver, link, counter)
            
            #raise Exception("Test")
            
        except NoSuchElementException:
            print('some error')
            #raise Exception("Test")
         
        # testing    
        #raise Exception("Test")    
            
        print('------------------------------------------------------------------------------------------------')
        print('\n')
    
    print("Done!!")    

    driver.quit()


def main():
    li_links= [
        'https://www.linkedin.com/in/ashwinnavaneedan/'
        ]
        
    login_and_create_base(li_links)
    

if __name__ == '__main__':
    main()