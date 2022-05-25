import json
import csv
import ast 

with open('main_content.json', encoding="utf8") as json_file:
    jsondata = json.load(json_file)
 
jsondata = ast.literal_eval(jsondata)
data_file = open('main_content.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()




# import ast 
# import json
# import csv

# with open("main_content.json", encoding="utf8") as file:
#     jsondata = json.load(file)

# jsondata = ast.literal_eval(jsondata)

# with open("main_content.csv", "w") as file:
#     csv_file = csv.writer(file)
#     for item in jsondata:
#         fields = list(item['fields'].values())
#         csv_file.writerow([item['pk'], item['model']] + fields)