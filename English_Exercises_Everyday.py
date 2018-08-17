import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
import time
import os

print("Hi, welcome to english exercise everyday service!")

second = int(input("How much time do you think you need to solve the exercise (in second): "))
print("OK, Let Start!")
page = requests.get('https://www.myenglishpages.com/site_php_files/exercises.php')
soup = BeautifulSoup(page.content,'html.parser')
menu = soup.find(class_="menu_table_1")
lessons = menu.findAll('a')
continues = 'y'

driver = webdriver.Chrome(executable_path='chromedriver.exe')
while 'y' in continues:
    url = "https://www.myenglishpages.com/site_php_files/"+str(random.choice(lessons)['href'])
    print(url)
    driver.get(url)
    time.sleep(second)
    #scoll down to the check ans but don't need to click it
    driver.find_element_by_id('check').click()
    soup_2 = BeautifulSoup(driver.page_source,'html.parser')
    result = soup_2.findAll("strong")
    print(result[-1].text,result[-3].text,result[-2].text)
    continues = str(input("Do you want to do another exercise? (Y/N): ")).lower()

print('Good bye! Remember what you have learned today!')
driver.quit()
os.system('cls' if os.name == 'nt' else 'clear')