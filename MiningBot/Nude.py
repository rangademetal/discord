from selenium import webdriver
from Database.Connect import Connection

import time
import random

db = Connection('localhost', 'root', 'Sad1996.', 'discord2')
database = db.connect()

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
try:
    while True:
        driver.get('https://www.pornpics.com/babe/')
        SCROLL_PAUSE_TIME = 0.5
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        i = random.randint(1, 841)
        click = driver.find_element_by_xpath(f'//*[@id="tiles"]/li[{i}]/a/img')
        click.click()
        link_galley = driver.current_url
        time.sleep(1)
        click = driver.find_element_by_xpath('//*[@id="main"]/div/span[1]/span')
        click.click()

        time.sleep(1)

        slider = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]')

        arr = slider.text.split('/')
        arr = arr[-1].strip()
        ran = random.randint(1, int(arr))
        driver.execute_script("window.history.go(-1)")
        driver.get(link_galley)
        time.sleep(1)
        click = driver.find_element_by_xpath(f'//*[@id="tiles"]/li[{ran}]')
        click.click()

        link = driver.current_url
        time.sleep(1)
        db.insert_nude(database, link)
except Exception as e:
    print(f'{e}')
