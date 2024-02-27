from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from time import sleep
from threading import Thread
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
import json

def Find_Element(driver : webdriver.Chrome, by, value : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            pass
        sleep(0.1)
    return element

def Find_Elements(driver : webdriver.Chrome, by, value : str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(by, value)
            if len(elements) > 0:
                break
        except:
            pass
        sleep(0.1)
    return elements

def Send_Keys(element : WebElement, content : str):
    element.clear()
    for i in content:
        element.send_keys(i)
        sleep(0.1)

service = Service(executable_path="C:\chromedriver-win64\chromedriver.exe")   
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9030")
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.magazineluiza.com.br/automotivo/l/au/')

output = []
total_company = 0
min = 6530000
max = 9999900
dis = 500000
for price in range(min, max, dis):
    try:
        min_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="price-range-min-input"]')
        min_price = Send_Keys(min_input, f'{price}')
        max_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="price-range-max-input"]')
        max_price = Send_Keys(max_input, f'{price + dis}')
        button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="price-range-apply-btn"]')
        driver.execute_script("arguments[0].click();", button)
        print('done')
        sleep(1)
        categories = Find_Elements(driver, By.XPATH, '//*[@id="__next"]/div/main/section[3]/div[3]/div')
        for category in categories:
            category_names = category.text.split('\n')
            if category_names[0] == 'Vendido por':
                try:
                    add_button = category.find_element(By.TAG_NAME, 'button')
                    driver.execute_script("arguments[0].click();", add_button)
                except:
                    pass
                company_names = category.find_elements(By.TAG_NAME, 'li')
                print(f'{price} ~ {price + dis} : company_number --> {len(company_names)}')
                cur_num = len(company_names)
                total_company += cur_num
                print(total_company)
                for company_name in company_names:
                    print(company_name.text)
                    output.append({'company_name' : company_name.text})
                break
        with open(f'output({min}-{max}).json', 'w') as file:
            json.dump(output, file)
        print('done')
        # driver.delete_all_cookies()
        driver.back()
        sleep(1)
    except:
        pass