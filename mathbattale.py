import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
try:
    driver.get("https://tbot.xyz/math/#eyJ1Ijo1MTk5ODQ5MDcsIm4iOiIuICIsImciOiJNYXRoQmF0dGxlIiwiY2kiOiIyMDUwNTk3MTkyNDkzODM4MDM4IiwiaSI6IkJBQUFBSUFzQXdEWklTaXk5WWVVUV9FbEZkZyJ9NDViN2U4N2FhOTAyZjE4ZDVhM2ZiMGYzMTZkZjQxMzY=")
except:
    pass

time.sleep(3)
i=0
while True and i<100:
    i+=1
    task = driver.find_element_by_css_selector("#task")
    x = task.find_element_by_id('task_x').text.strip()
    op = task.find_element_by_id('task_op').text.replace('–', '-').replace('×', '*').replace('/', '//').replace('+', '+').strip()
    y = task.find_element_by_id('task_y').text.strip()
    res = task.find_element_by_id('task_res').text.strip()
    try:
        if eval("%s %s %s" % (x, op, y)) != int(res):
            driver.find_element_by_id('button_wrong').click()
        else:
            driver.find_element_by_id('button_correct').click()
    except:
        print(x,op,y,res)
        import os
        os.system('play --no-show-progress --null --channels 1 synth 1 sine 440')
        break

    time.sleep(.2)
