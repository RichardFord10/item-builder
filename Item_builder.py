from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import re
import pandas as pd
import sys
import csv
import os

# configure webdriver & headless chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options = chrome_options, executable_path=r'C:/Users/rford/Desktop/chromedriver/chromedriver.exe')

# current day format
currentDate = datetime.today().strftime('%Y-%m-%d')

def login(user, pword = str):
    driver.get("https://###.com/manager")
    Username = driver.find_element_by_id("bvuser")
    Password = driver.find_element_by_id("bvpass")
    Login = driver.find_element_by_xpath('//*[@id="form1"]/div/div[2]/input')
    Username.send_keys(user)
    Password.send_keys(pword)
    Login.click()
    print("Logging In...")
 
#read csv and turn number column into list
df = pd.read_csv(r'C:/Users/rford/Desktop/items.csv')
item_number_list = df["item_nums"].tolist()



def make_list():
    driver.get("https://www.#######.com/manager/itemsManager.php")
    WebDriverWait(driver, 3)
#check 'Either' radio button on Currently Active
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form[1]/div/ul/li[2]/input[3]').click()
#check 'Either' radio button on Sold Online
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form[1]/div/ul/li[1]/input[3]').click()
#check 'Either' radio button on Sold to Customers
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form[1]/div/ul/li[3]/input[3]').click()
#check 'Either' radio button on Sales Taxable
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form[1]/div/ul/li[4]/input[3]').click()

    #do for each item num
    for item_number in item_number_list:
    #clear Search bar
        driver.find_element_by_xpath('//*[@id="itemname"]').clear()
        WebDriverWait(driver, 10)
    #send item ID to Search Bar
        driver.find_element_by_xpath('//*[@id="itemname"]').send_keys(item_number)
        WebDriverWait(driver, 10)
    #Submit Search
        driver.find_element_by_xpath('//*[@id="searchinputs"]/div/div[2]/div[3]/input[3]').submit()
        WebDriverWait(driver, 10)
    #Declare ID for add to list button
        add_to_list_id = 'addToList_{}'.format(item_number)
    #wait for add to list button to appear and click on it
        ignored_exceptions=(NoSuchElementException, StaleElementReferenceException)
        add_to_list = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, add_to_list_id)))
        add_to_list.click()
        WebDriverWait(driver, 5)
        print('Item {} has been added to List!'.format(item_number))
    print('All Items added to List!')
              

login(input("Enter Username: "), getpass("Enter Password: "))
make_list()
WebDriverWait(driver, 10)
