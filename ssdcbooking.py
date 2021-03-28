from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pynotifier import Notification
import time
import os

PATH = r"C:\Users\ngokj\Desktop\ssdc2\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ssdcl.com.sg/User/Login")

ssdc_user = driver.find_element_by_id('UserName')
ssdc_user.send_keys(os.environ.get('ssdc_user'))

ssdc_password = driver.find_element_by_id('Password')
ssdc_password.send_keys(os.environ.get('ssdc_password'))

login_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/form/div[5]/div/button').click()
print("LOGGED IN")

booking_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/ul/li[3]/a').click()

newbooking_button = driver.find_element_by_id('btnNewBooking').click()

checkproceed_button = driver.find_element_by_id('chkProceed').click()

proceed_button = driver.find_element_by_id('lnkProceed').click()

availability_button = driver.find_element_by_id('btn_checkforava').click()

time.sleep(2)

buyButton = False
while not buyButton:
    try:
        cartout = driver.find_element_by_class_name('slotBooking')
        print('clicked hurry')
        cartout.click()
        Notification(
            title='ssdc slot found',
            description='hurry pay',
            duration= 20,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
        time.sleep(90)

    except (NoSuchElementException) as e:
        print('no slots:(')
        driver.execute_script('location.reload()')
        time.sleep(90)

