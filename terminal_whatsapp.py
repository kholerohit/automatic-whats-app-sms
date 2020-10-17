from selenium import webdriver
import datetime
import time
driver = webdriver.Firefox(executable_path='/home/khole/Downloads/gk/geckodriver')
driver.get('https://web.whatsapp.com/')
while 1:
    j = 1
    print("*******************************************************************")
    name = input('Enter Name: ')
    name = name.split(',')
    msg = input('Enter msg: ')
    count = int(input('no. of times: '))
    input('Enter anything')
    print('Sending ...')
    for item in name:
        time.sleep(1)
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(item))
        user.click()
        msg_box = driver.find_element_by_class_name('_3u328')
        for i in range(count):
            msg_box.send_keys("{}.  {}  {}".format(i+1, msg, str(datetime.datetime.now())[11:11]))
            button = driver.find_element_by_class_name('_3M-N-')
            button.click()
