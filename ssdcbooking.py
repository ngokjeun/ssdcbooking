from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pynotifier import Notification
import time
import os
import requests

#booking_date in dd/m/yy
booking_date = "24/4/21"

PATH = r"C:\Users\ngokj\Desktop\ssdc2\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def navig():
    driver.get("https://www.ssdcl.com.sg/User/Login")
    ssdc_user = driver.find_element_by_id('UserName')
    ssdc_user.send_keys(os.environ.get('ssdc_user'))
    ssdc_password = driver.find_element_by_id('Password')
    ssdc_password.send_keys(os.environ.get('ssdc_password'))
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/form/div[5]/div/button').click() #login 
    print('logged in')
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/ul/li[3]/a').click() #booking 
    driver.find_element_by_id('btnNewBooking').click() #new booking
    driver.find_element_by_id('chkProceed').click() #check proceed
    driver.find_element_by_id('lnkProceed').click() #proceed
    driver.find_element_by_id('btn_checkforava').click() #availability
    time.sleep(2)

def clickslot():
    buyButton = False
    while not buyButton:
        try:
        #book first slot within the week
            #cartout = driver.find_element_by_class_name('slotBooking')
        #book specific date
            cartout = driver.find_element_by_xpath('//a[@class="slotBooking"][contains(@id, booking_date)]')
            print('clicked, pay now')
            cartout.click()
            Notification(
                title='ssdc slot found',
                description='hurry pay',
                duration= 30,
                urgency=Notification.URGENCY_CRITICAL
            ).send()
            #ifttt integration with maker, connect own ifttt account
            requests.get('https://maker.ifttt.com/trigger/clicked/with/key/ddg9gyPPaIJ-1sJWzMpsI_')
            time.sleep(60)

        except (NoSuchElementException):
            print('no slots:(')
            driver.execute_script('location.reload()')
            time.sleep(60)

def main():
    navig()
    clickslot()

main()