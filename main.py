from selenium import webdriver
import sys
import time
import log
from selenium.webdriver.chrome.options import Options

url = sys.argv[1]

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
log.good("Browser started.")

new_btn_xpath = '//*[@id="app"]/div[2]/div[1]/button'
title_xpath = '//*[@id="wish-new"]/div/div[1]/section/div/textarea'
editor_xpath = '//*[@id="wish-new"]/div/div[1]/section/div/div/trix-editor'
header_xpath = '//*[@id="surface-header"]/div[3]/div/div/h1'

while True:
    new_btn = browser.find_element_by_xpath(new_btn_xpath)
    new_btn.click()
    browser.implicitly_wait(.01)
    title_area = browser.find_element_by_xpath(title_xpath)
    title_area.send_keys("bruh")
    browser.implicitly_wait(.01)
    editor_area = browser.find_element_by_xpath(editor_xpath)
    editor_area.send_keys("bruh")
    browser.implicitly_wait(.01)
    header = browser.find_element_by_xpath(header_xpath)
    header.click()
    browser.implicitly_wait(.01)