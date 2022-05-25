# "https://www.mayoclinic.org/diseases-conditions/index?letter=A"
# site = "https://www.mayoclinic.org/diseases-conditions/index?letter="

# for i in range(65,91): 
#     upper_alphabet = chr(i) 


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrolme(executable_path="C:\EV_Files\ChromeDriver\chromedriver.exe")
# driver.maximize_window()

mainsite = "https://www.mayoclinic.org/diseases-conditions"
inner_site = "https://www.mayoclinic.org/diseases-conditions/index?letter="
# driver.get("site")
all_alpha_site = []

for i in range(65,91): 
    upper_alphabet = chr(i)
    all_alpha_site.append(inner_site+str(upper_alphabet))

print(all_alpha_site)

# for i in all_alpha_site:
    





    # time.sleep(2)
    # driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    # driver.find_element_by_class_name("_3704LK").click()
    # driver.find_element_by_class_name("_3704LK").send_keys("mobiles")
    # driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
