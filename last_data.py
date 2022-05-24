import requests
from bs4 import BeautifulSoup

with open('last_data.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

    print(soup.find("h1").find("a").text)

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


    for k in list(main_obj.keys()):
        try:
            if len(main_obj[k])<1:
                del main_obj[k]
        except: 
            pass

    del main_obj["Mayo Clinic Footer"]
    del main_obj["Advertising"]
    del main_obj["Legal Conditions and Terms"]
    

    # new_obj = {
    #     "Diagnosis":main_obj["Diagnosis"],
    #     "Treatment":main_obj["Treatment"],
    # }

    # import json
    # with open('data.json', 'w', encoding='utf-8') as f:
        # json.dump(new_obj, f, ensure_ascii=False, indent=4)
        # json.dump(main_obj, f, ensure_ascii=False, indent=4)
