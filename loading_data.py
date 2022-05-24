import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
# print(data["A"][0]["Atrial fibrillation"]["Diagnosis"])
# print(data["A"][0]["Atrial fibrillation"]["Treatment"])
  
print(len(data["A"]))

# Closing file
f.close()