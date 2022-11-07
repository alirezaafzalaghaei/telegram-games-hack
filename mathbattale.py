import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
try:
    driver.get("https://t.me/gamebot?game=MathBattle")
except:
    pass

time.sleep(3)
i=0
MAX_RECORD = 100
while True and i<MAX_RECORD:
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
