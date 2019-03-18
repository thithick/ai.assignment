from selenium import webdriver
import time #to enable sleep
import getpass # invincible password input in CMD

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2} #to get rid of the chrome popup
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com')
assert 'Facebook' in driver.title
driver.maximize_window()

# elemE = driver.find_element_by_id('email')
# elemE.send_keys("frog.qa.team@gmail.com") #facebook email

# elemP = driver.find_element_by_id('pass')
# elemP.send_keys("frog2012") #facebook pass

# code below is to use different Facebook Acc (require input from user)
elemE = driver.find_element_by_id('email') #to find email field
id = raw_input("Please enter your Email: ") #enter email id in cmd
elemE.send_keys(id)

elemP = driver.find_element_by_id('pass') # to find password field
pw = getpass.getpass("Please enter your password: ") # enter password in cmd (invincible)
elemP.send_keys(pw)

driver.find_element_by_id('loginbutton').click() # click login button

newNotifCount1 = driver.find_element_by_id("notificationsCountValue").get_attribute('innerText') # to get the notification count number
newNotifCount2 = int(newNotifCount1)
notif = driver.find_element_by_id("fbNotificationsJewel")
print (newNotifCount1)# to display notification number
if newNotifCount2 > 0:
    notif.click()
    time.sleep(5)
    topNotif = driver.find_element_by_xpath("//div[@class='uiScrollableAreaContent']")
    topNotif.find_elements_by_tag_name("li")[0].click()
    time.sleep(60) # wait for 1 minute when notification available
    driver.find_element_by_id('userNavigationLabel').click() # click arrow option
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(text(),'Log out')]").click() # click logout
else:
        newMessageCount1 = driver.find_element_by_id("mercurymessagesCountValue").get_attribute('innerText') # to get the notification count number
        newMessageCount2 = int(newMessageCount1)
        print (newMessageCount1) # to display notification number
        sideMessage = driver.find_element_by_id('navItem_217974574879787')
        if newMessageCount2 > 0:
            sideMessage.click()
            time.sleep(5)
            topMsg = driver.find_element_by_xpath("//div[@class='uiScrollableAreaContent']")
            topMsg.find_elements_by_tag_name("li")[0].click()
            time.sleep(157)
            driver.find_element_by_id('userNavigationLabel').click() # click arrow option
            time.sleep(2)
            driver.find_element_by_xpath("//*[contains(text(),'Log out')]").click()

        else:
            driver.find_element_by_id('userNavigationLabel').click() # click arrow option
            time.sleep(2)
            driver.find_element_by_xpath("//*[contains(text(),'Log out')]").click()






