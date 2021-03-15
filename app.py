from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
url = 'https://www.instagram.com/'
driver.get(url)
sleep(30)

def find_follow_button(buttons):
    for button in buttons:
        if button.text == 'Follow':
            classes = button.get_attribute('class')
            if '_4pI4F' in classes:
                continue
            return button
    
    return None



def follow(array_users, driver):
    for link in array_users:
        try:
            driver.get(link)
            buttons = driver.find_elements_by_tag_name('button')
            button = find_follow_button(buttons)
            if button != None:
                button.click()
            sleep(2)
        except Exception as e:
            print(e)
            
#! Add instagram accounts here
#* Example
#instaAccounts_String='''instagram.com/nickname
#instagram.com/nickname2
#'''
instaAccounts_String = '''
 '''


instaAccounts = instaAccounts_String.split('\n')
sleep(3)
follow(instaAccounts,driver)
