import requests
from bs4 import BeautifulSoup

all_href_links = []

with open('data1.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    div_tag = soup.find_all("div",{"id":"index"})[0]
    ol_tag = div_tag.find("ol")
    li_tag = ol_tag.find_all("li")

    for li_data in li_tag:
        a_tag = li_data.find("a")
        all_href_links.append("https://www.mayoclinic.org"+a_tag['href'])

    print(all_href_links)