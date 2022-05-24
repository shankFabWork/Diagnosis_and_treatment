import requests
from bs4 import BeautifulSoup


with open('single_data.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    # a_tag = soup.find_all("a",{"id":"et_genericNavigation_diagnosis-treatment"})
    # Diagnosis_and_treatment_link_getter = "https://www.mayoclinic.org"+a_tag[0]['href']
    # print(Diagnosis_and_treatment_link_getter)

    # a_tag = soup.find_all("ul",{"role":"menubar"})[1]
    # final_li_tag = soup.find_all("li",{"role":"menuitem"})[1]
    # print(final_a_tag)
    # Diagnosis &amp; treatment
    a_tag = soup.find_all("a", string="Diagnosis & treatment")
    print(final_li_tag)