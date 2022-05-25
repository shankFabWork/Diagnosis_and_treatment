import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# import chromedriver_autoinstaller as chromedriver
# chromedriver.install()
# driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")

from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import json

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
# driver = webdriver.Firefox(executable_path="geckodriver.exe")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.mayoclinic.org/diseases-conditions")

# getting link from A-Z
inner_site = "https://www.mayoclinic.org/diseases-conditions/index?letter="

# all_alpha_site = []
# for i in range(65,91): 
#     upper_alphabet = chr(i)
#     all_alpha_site.append(inner_site+str(upper_alphabet))

# print(all_alpha_site)
############################
final_main_obj = {}


a_z_zero_arr = [*range(65,91)]
a_z_zero_arr.append(str(0))
for i in a_z_zero_arr:
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    # This is Current Alphabet
    try:
        if i == 0 or i == '0':
            curr_alphabet = str(0)
        else:
            curr_alphabet = str(chr(i))


        driver.get(inner_site+curr_alphabet)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'lxml')

        # Initlizing Final Main Object
        final_main_obj[curr_alphabet] = []

        # Collect Links of all disease Array 
        all_href_links = []

        # print("--")
        # div_tag = soup.find("div",{"id":"index"})
        # print(div_tag)
        ol_tag = soup.find_all("ol")[1]
        li_tag = ol_tag.find_all("li")
        # print(li_tag)

        # Alphabet 
        alphabet_name = curr_alphabet
        
        for li_data in li_tag:
            a_tag = li_data.find("a")
            all_href_links.append("https://www.mayoclinic.org"+a_tag['href'])

        # print(all_href_links)

        for i in all_href_links:
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
            driver.get(i)

            try:
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'lxml')            

                # Click on Diagnosis & treatment
                a_tag = soup.find_all("a",{"id":"et_genericNavigation_diagnosis-treatment"})
                Diagnosis_and_treatment_link_getter = "https://www.mayoclinic.org"+a_tag[0]['href']
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
                driver.get(Diagnosis_and_treatment_link_getter)

                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'lxml')

                # Click on Print
                div_tag = soup.find_all("div",{"id":"phmaincontent_0_ctl01_divByLine"})[0]
                div1_tag = div_tag.find_all("div",{"class":"print"})[0]
                a_tag = div1_tag.find("a")
                Diagnosis_and_treatment_link_getter = "https://www.mayoclinic.org"+a_tag['href']
                print(Diagnosis_and_treatment_link_getter)

                # Getting Data Within Specific Diseases Print Page
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
                driver.get(Diagnosis_and_treatment_link_getter)

                # Converting Soup to HTML Page
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'lxml')
                # print(soup)

                # This is Heading or Disease Name
                disease_heading = soup.find("h1").find("a").text

                # Initializing Variables
                main_obj = {}
                flag = 0
                data = ""
                curr_text_name = ""

                for i in soup.find_all():
                    if i.name == "h2" or i.name == "h3":

                        main_obj[curr_text_name] = data
                        curr_tag_name = i.name
                        curr_text_name = i.text

                        main_obj[curr_text_name] = {}

                        flag = 1
                    elif str(i.name) != "h2" and flag == 1:
                        data += str(str(i.text)+"\n")

                # Removing empty string keys
                for k in list(main_obj.keys()):
                    try:
                        if len(main_obj[k])<1:
                            del main_obj[k]
                    except: 
                        pass

                # Removing uneccesary keys
                del main_obj["Mayo Clinic Footer"]
                del main_obj["Advertising"]
                del main_obj["Legal Conditions and Terms"]
                del main_obj["Mayo Clinic Privacy Policy"]

                final_main_obj[curr_alphabet].append({disease_heading:main_obj})

                
     
            except:
                pass
            
    except:
        pass





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
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(final_main_obj, f, ensure_ascii=False, indent=4)

drive.close()




