from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ssdcl.com.sg/User/Login")

user_input = driver.find_element_by_id('UserName')
user_input.send_keys('xxx')

password_input = driver.find_element_by_id('Password')
password_input.send_keys('xxx')

login_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/form/div[5]/div/button')
login_button.click()

print("LOGGED IN")

booking_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/ul/li[3]/a').click()

newbooking_button = driver.find_element_by_id('btnNewBooking').click()

checkproceed_button = driver.find_element_by_id('chkProceed').click()

proceed_button = driver.find_element_by_id('lnkProceed').click()

#extra-------------------------------------------------------------------------------------------------------------
#earliestdate_button = driver.find_element_by_id('button-searchDate').click()
#time.sleep(1)
#selecteddate_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/form/div[4]/div/input')
#print(selecteddate_button.get_attribute('value'))

#time.sleep(1)
#extra-------------------------------------------------------------------------------------------------------------

availability_button = driver.find_element_by_id('btn_checkforava').click()

time.sleep(2)

buyButton = False

while not buyButton:
        try:
            cartout = addButton = driver.find_element_by_class_name('slotBooking')
            print('clicked hurry')
            cartout.click()
            continue


        except (NoSuchElementException) as e:
            print('no slots:(')
            driver.execute_script("location.reload()")
            time.sleep(60)
            continue


