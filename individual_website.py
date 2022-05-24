import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:\EV_Files\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mayoclinic.org/diseases-conditions/index?letter=A")
time.sleep(2)

# Selenium visits each Job Title page
# python_button = driver.find_element_by_class_name('fnt-14 lnk-hvr block of-hid ht-name')
# python_button.click() #click link

# html_content = driver.page_source
# soup = BeautifulSoup(html_content, 'lxml')
# car_name = soup.find_all("a",{"class":"fnt-14 lnk-hvr block of-hid ht-name"})
# car_price = soup.find_all("div",{"class":"b fnt-black fnt-14"})
# car_details = soup.find_all("div",{"class":"clr-try fnt-12 pb-10 ht-spec of-hid"})

# for i in range(len(car_name)):
#     print(car_name[i].text +" "+ car_price[i].text)
    
#     s = car_details[i].text

#     splitted_data = (s.split("|"))
#     for i in splitted_data:
#         if i.find("km/charge") != -1:
#             new_str = i
#             s_word = "|"
#             e_word = "km/charge"
#             start = new_str.find(s_word) + len(s_word)
#             end = new_str.find(e_word)
#             substring = new_str[start:end]
#             print(substring)
            
# print(panel_heading_data)

# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL + 't')

# https://www.mayoclinic.org/diseases-conditions/atrial-fibrillation/symptoms-causes/syc-20350624
# https://www.mayoclinic.org/diseases-conditions/atrial-fibrillation/diagnosis-treatment/drc-20350630

# https://www.mayoclinic.org/diseases-conditions/abdominal-aortic-aneurysm/symptoms-causes/syc-20350688
# https://www.mayoclinic.org/diseases-conditions/abdominal-aortic-aneurysm/diagnosis-treatment/drc-20350693

