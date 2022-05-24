import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:\EV_Files\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mayoclinic.org/diseases-conditions")



# getting link from A-Z
inner_site = "https://www.mayoclinic.org/diseases-conditions/index?letter="
all_alpha_site = []

for i in range(65,91): 
    upper_alphabet = chr(i)
    all_alpha_site.append(inner_site+str(upper_alphabet))

# print(all_alpha_site)
############################

for i in all_alpha_site:
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get(i)
    # print(i)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')

    all_href_links = []

    # print("--")
    # div_tag = soup.find("div",{"id":"index"})
    # print(div_tag)
    ol_tag = soup.find_all("ol")[1]
    li_tag = ol_tag.find_all("li")
    # print(li_tag)
    
    for li_data in li_tag:
        a_tag = li_data.find("a")
        all_href_links.append("https://www.mayoclinic.org"+a_tag['href'])

    # print(all_href_links)

    for i in all_href_links:
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(i)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'lxml')

        a_tag = soup.find_all("a",{"id":"et_genericNavigation_diagnosis-treatment"})
        Diagnosis_and_treatment_link_getter = "https://www.mayoclinic.org"+a_tag[0]['href']

        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(Diagnosis_and_treatment_link_getter)
        # html_content = driver.page_source
        # soup = BeautifulSoup(html_content, 'lxml')

        # a_tag = soup.find_all("ul",{"role":"menubar"})[1]
        # final_li_tag = soup.find_all("li",{"role":"menuitem"})[1]
        # print(final_a_tag)

    # print("--")

    # div_tag = soup.find_all("div",{"id":"index"})[0]
    # ol_tag = div_tag.find("ol")
    # li_tag = ol_tag.find_all("li")

    # for li_data in li_tag:
    #     a_tag = li_data.find("a")
    #     all_href_links.append("https://www.mayoclinic.org"+a_tag['href'])

    # print(all_href_links)


    # a_tag = soup.find_all("a",{"id":"et_genericNavigation_diagnosis-treatment"})
    # a_tag = soup.find_all("a", string="Diagnosis & treatment")
    # a_tag = soup.findall("ul",{"role":"menubar"})[2]
    # final_a_tag = a_tag.find_all("li",{"role":"menuitem"})
    # print(final_a_tag)
    # a_tag = soup.find_all("a", string="Diagnosis & treatment")

    # Diagnosis_and_treatment_link_getter = "https://www.mayoclinic.org"+a_tag[0]['href']
    # print(Diagnosis_and_treatment_link_getter)


drive.close()




