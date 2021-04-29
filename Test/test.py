from selenium import webdriver
import time
import random

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://www.pornpics.com/galleries/beautiful-redhead-vos-holds-her-firm-tits-after-taking-off-sensual-lingerie/')
time.sleep(1)
clicker = driver.find_element_by_xpath('//*[@id="main"]/div/span[1]/span')
clicker.click()
time.sleep(1)

slider = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]')

arr = slider.text.split('/')
arr = arr[-1].strip()
ran = random.randint(1, int(arr))
