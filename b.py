import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:\EV_Files\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cartrade.com/new-cars/best-electric-cars-in-india/")
time.sleep(2)

# Selenium visits each Job Title page
# python_button = driver.find_element_by_class_name('fnt-14 lnk-hvr block of-hid ht-name')
# python_button.click() #click link

html_content = driver.page_source
soup = BeautifulSoup(html_content, 'lxml')
car_name = soup.find_all("a",{"class":"title_link"})

final_data = {}



all_car_soup = []
for i in range(len(car_name)):
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    driver.get('https://www.cartrade.com'+car_name[i]['href'])
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')



    # table_data = all_car_soup[i].find("div",{"class":"keySpecsTable"})
    car_title = soup.find("h1",{"class":"model-overview-title"}).text

    # Initailize final_data object
    final_data[car_title] = []

    print("-----------------------------------------")
    print(car_title)
    print("-----------------------------------------")
    for j in soup.find_all("tr",{"class":"keySpecsRow"}):
        a = j.find("th").find("h3")
        b = j.find("td")
        print(a.text+" --> "+b.text)
        # print(b.text)
        # print("-----")
        # final_data[car_title].append({a.text:b.text})
        final_data[car_title].append({a.text:b.text})


    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
    print(car_name[i].text+" "+car_name[i]['href'])
            
print(final_data)
# print(all_car_soup)
# print(panel_heading_data)

# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL + 't')


# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
# driver.get('https://www.cartrade.com/'+)
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 



